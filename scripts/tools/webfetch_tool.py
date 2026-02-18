#!/usr/bin/env python3
"""webfetch_tool: Controlled HTTP(S) fetch with strict safety gates.

Goals:
- Provide minimal capability for agents needing to inspect remote HTML/text
- Disabled by default to avoid accidental outbound network calls
- Enforce explicit opt-in via CLI flag or environment variable
- Limit response size and strip binary content risk (text only)

Activation:
- Set env OPENCODE_ALLOW_WEB=1 OR pass --allow explicitly

Behavior:
- Only allows URLs beginning with http:// or https://
- Fetches using stdlib urllib; no redirects beyond a small chain (default 5)
- Captures status code, final URL, and at most N bytes of UTF-8 text
- If content-type indicates binary (e.g., application/octet-stream, image/*) -> abort
- Truncates large responses and reports truncated: true

Return JSON fields:
  url, final_url, status, bytes, truncated, content (if text), error (if any)

Note: This is intentionally minimal; richer parsing (HTML->markdown) can be layered later.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from typing import Dict, Any, Tuple

MAX_DEFAULT_BYTES = 100_000  # 100 KB cap
MAX_REDIRECTS = 5
BINARY_PREFIXES = ("image/", "video/", "audio/", "application/octet-stream")
TEXT_LIKE = ("text/", "application/json", "application/javascript", "application/xml")


def allowed() -> bool:
    return os.environ.get("OPENCODE_ALLOW_WEB") == "1"


def classify_content_type(ct: str | None) -> str:
    if not ct:
        return "unknown"
    lower = ct.lower()
    if any(lower.startswith(p) for p in BINARY_PREFIXES):
        return "binary"
    if any(lower.startswith(p) for p in TEXT_LIKE):
        return "text"
    return "other"


class LimitedRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self, max_redirects: int) -> None:
        self.max_redirects = max_redirects
        self.redirects = 0

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.redirects += 1
        if self.redirects > self.max_redirects:
            raise urllib.error.HTTPError(
                req.full_url,
                code,
                f"Too many redirects (>{self.max_redirects})",
                headers,
                fp,
            )
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_once(
    url: str, timeout: int, limit: int
) -> Tuple[int, str, bytes, str | None, bool]:
    req = urllib.request.Request(url, headers={"User-Agent": "opencode-webfetch/0.1"})
    redirect_handler = LimitedRedirectHandler(MAX_REDIRECTS)
    opener = urllib.request.build_opener(redirect_handler)

    with opener.open(req, timeout=timeout) as resp:  # nosec B310 (controlled destination)
        status = getattr(resp, "status", 200)
        final_url = resp.geturl()
        ctype = resp.headers.get("Content-Type")

        classification = classify_content_type(ctype)
        if classification == "binary":
            raise ValueError(f"Refusing binary content type: {ctype}")

        chunk_size = 8192
        max_bytes = max(limit, 0)
        chunks: list[bytes] = []
        bytes_read = 0
        truncated = False

        while True:
            chunk = resp.read(chunk_size)
            if not chunk:
                break

            remaining = max_bytes - bytes_read
            if remaining <= 0:
                truncated = True
                break

            if len(chunk) > remaining:
                chunks.append(chunk[:remaining])
                bytes_read += remaining
                truncated = True
                break

            chunks.append(chunk)
            bytes_read += len(chunk)

    return status, final_url, b"".join(chunks), ctype, truncated


def run_fetch(url: str, allow: bool, limit: int, timeout: int) -> Dict[str, Any]:
    if not allow and not allowed():
        return {"error": "webfetch disabled (set OPENCODE_ALLOW_WEB=1 or pass --allow)"}
    if not (url.startswith("http://") or url.startswith("https://")):
        return {"error": f"Only http(s) URLs allowed: {url}"}

    try:
        status, final_url, data, ctype, truncated = fetch_once(url, timeout, limit)
    except urllib.error.HTTPError as e:
        return {
            "error": f"HTTP error {e.code}: {e.reason}",
            "status": e.code,
            "url": url,
        }
    except urllib.error.URLError as e:
        return {"error": f"Connection error: {e.reason}", "url": url}
    except ValueError as e:
        return {"error": str(e), "url": url}
    except Exception as e:  # pragma: no cover
        return {"error": f"Unexpected error: {e}", "url": url}

    classification = classify_content_type(ctype)
    if classification == "binary":
        return {
            "error": f"Refusing binary content type: {ctype}",
            "status": status,
            "url": url,
        }

    # Attempt UTF-8 decode with fallback replace
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        text = data.decode("utf-8", errors="replace")

    if classification not in ("text", "other", "unknown"):
        return {"error": f"Unsupported content type: {ctype}"}

    return {
        "url": url,
        "final_url": final_url,
        "status": status,
        "bytes": len(data),
        "truncated": truncated,
        "content_type": ctype,
        "content": text,
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Controlled remote fetch (text only)")
    parser.add_argument("--url", required=True, help="HTTP(S) URL to fetch")
    parser.add_argument(
        "--allow",
        action="store_true",
        help="Override safety gate (or set OPENCODE_ALLOW_WEB=1)",
    )
    parser.add_argument(
        "--limit", type=int, default=MAX_DEFAULT_BYTES, help="Max bytes (default 100k)"
    )
    parser.add_argument(
        "--timeout", type=int, default=10, help="Timeout seconds (default 10)"
    )
    args = parser.parse_args(argv)

    result = run_fetch(args.url, args.allow, args.limit, args.timeout)
    print(json.dumps(result, indent=2))
    return 0 if "error" not in result else 1


if __name__ == "__main__":  # pragma: no cover
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        print("Interrupted", file=sys.stderr)
        sys.exit(130)

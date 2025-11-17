---
id: task-1
title: Relax lint rules for optional agent model fields
status: To Do
assignee: []
created_date: '2025-11-17 04:16'
labels: []
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Allow agents to omit explicit model entries so they can inherit defaults from opencode.json.
Update lint script configuration and docs accordingly.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Lint passes when agent frontmatter omits model
- [ ] #2 Required keys (description/mode/temperature/tools) remain enforced
<!-- AC:END -->

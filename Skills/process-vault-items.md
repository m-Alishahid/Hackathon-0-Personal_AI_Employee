---
name: process-vault-items
description: |
  Reads all pending .md files in /Needs_Action, creates Plan.md files,
  updates Dashboard.md, and moves processed items to /Done.
---

# Process Vault Items Skill

## When to Use
Use this skill whenever there are files in `/Needs_Action/` or the user asks to "process inbox".

## Instructions
1. Read all files in `Needs_Action`
2. Decide what to do based on the file contents
3. Create a Plan in `Plans` folder
4. Move processed items to `Done`
5. Update `Dashboard.md`

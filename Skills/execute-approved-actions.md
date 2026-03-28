---
name: execute-approved-actions
description: |
  Checks the /Approved folder for human-approved files and executes the required external actions via the MCP server.
---

# Execute Approved Actions Skill

## When to Use
Use this skill when the user tells you to "check approved actions", "execute approvals", or when you notice files placed in the `Approved/` folder.

## Instructions
1. Read all files inside the `Approved/` folder.
2. For each file, identify what action is required (e.g., Post to LinkedIn, Send Email).
3. If it is a LinkedIn post:
   - Extract the content of the post.
   - Use your configured tools (or the `post_to_linkedin` MCP tool) to publish the post.
4. If the execution is successful:
   - Move the file from `Approved/` to `Done/`.
   - Update `Dashboard.md` to log the completed action.
   - Add an entry to the `Logs/` folder specifying the action taken.
5. If you do not have the MCP server connected, you can simulate the execution by using a local python script or noting it in the dashboard.

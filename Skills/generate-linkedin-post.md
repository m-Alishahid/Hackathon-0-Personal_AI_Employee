---
name: generate-linkedin-post
description: |
  Reads the scheduled trigger for a marketing post, drafts an engaging LinkedIn post,
  and saves it to Pending_Approval for human review.
---

# Generate LinkedIn Post Skill

## When to Use
Use this skill when you see a file in `Needs_Action` like `TRIGGER_Marketing_...md` or when the user asks you to write a marketing post.

## Instructions
1. Check `Business_Goals.md` to see what service or product we are currently promoting (e.g., Digital FTE solutions, Agentic AI consulting).
2. Draft an engaging, professional LinkedIn post that generates sales/leads. Include relevant hashtags.
3. Save the crafted post to the `Pending_Approval` folder.
   - Filename: `APPROVAL_LINKEDIN_POST_<date>.md`
   - Inside the file, clearly include the proposed text.
   - Add instructions for the human: *"Move this file to the `Approved` folder to publish it."*
4. Delete/Move the original trigger file from `Needs_Action` to `Done`.
5. Update `Dashboard.md` to show that a post is waiting for approval.

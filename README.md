# 🤖 Personal AI Employee — Silver Tier

> **Hackathon 0: Building Autonomous FTEs in 2026**
> *Your life and business on autopilot. Local-first, agent-driven, human-in-the-loop.*

---

## 📋 Tier Declaration
**SILVER TIER** — Functional Assistant

---

## 🚀 What's New in Silver Tier?
This iteration upgrades the basic AI employee by introducing a multi-watcher system, safe external actions via a mock MCP server, an autonomous scheduler, and a robust Human-in-the-Loop (HITL) approval process for sensitive actions like social media marketing.

### Silver Tier Features Achieved:
| Requirement | Status | Implementation Details |
|-------------|--------|------------------------|
| **Two or More Watchers** | ✅ | `filesystem_watcher.py` (Local files) & `linkedin_watcher.py` (LinkedIn) |
| **Auto Post to LinkedIn** | ✅ | Mock MCP executes LinkedIn posts safely |
| **Claude Reasoning Loop** | ✅ | Claude creates `Plan.md` files before running tasks |
| **Working MCP Server** | ✅ | `mcp_server.py` exposing `post_to_linkedin` |
| **HITL Approval Workflow** | ✅ | Use of `Pending_Approval/` and `Approved/` folders |
| **Basic Scheduling** | ✅ | `scheduler.py` handles autonomous time-based triggers |
| **All Functions as Skills**| ✅ | Located exactly in the `Skills/` directory |

---

## 🏗️ The Clean Architecture (Flat Design)

To strictly enforce a "Local First" accessible design, the entire ecosystem lives in a single flat folder structure. No convoluted Virtual Environments, no excessive nested `src/` folders. Pure functionality.

```
AI_Employee_Vault/
├── Inbox/                   ← Drop tasks/files here
├── Needs_Action/            ← Watchers auto-create MD files here
├── Pending_Approval/        ← Claude writes sensitive drafts here
├── Approved/                ← YOU drag files here to approve them
├── Done/                    ← Completed tasks move here
├── Plans/                   ← Claude creates Plan.md here
├── Logs/                    ← Audit logs and MCP output
├── Skills/                  
│   ├── generate-linkedin-post.md
│   ├── execute-approved-actions.md
│   └── process-vault-items.md
├── Dashboard.md             ← Live system status
├── Company_Handbook.md      ← Rules of engagement
├── filesystem_watcher.py    ← 🟢 Watcher 1
├── linkedin_watcher.py      ← 🟢 Watcher 2
├── scheduler.py             ← 🟢 Auto-Scheduler
├── mcp_server.py            ← 🟢 The MCP External Action Server
└── README.md                
```

---

## 🛠️ How to Run & Demo (Step-by-Step)

### Prerequisites
- Python installed (No special dependencies required!)
- Claude Code CLI installed

### Step 1: Start the Core Services
Open **3 terminal windows** inside the `AI_Employee_Vault` directory and start your Python processes:
1. `python filesystem_watcher.py`
2. `python linkedin_watcher.py`
3. `python scheduler.py`

*(Instantly, the scheduler will draft a `TRIGGER_...md` file into the `Needs_Action` folder, simulating a time-based task).*

### Step 2: Clause Processing (The Brain)
Open a 4th terminal for **Claude Code**:
```bash
claude
# Tell Claude: "Use your skills to process my inbox / Needs Action"
```
Claude will notice the marketing trigger, write a catchy LinkedIn post, and move it to the `Pending_Approval` folder. 

### Step 3: Human-in-the-Loop (HITL)
The AI drafted the post, but cannot publish it without YOU!
1. Open the `Pending_Approval/` folder.
2. Review the LinkedIn post.
3. Drag and drop the file into the `Approved/` folder.

### Step 4: External Action (MCP Execution)
Go back to the Claude terminal. 
```bash
# Tell Claude: "Check the Approved folder and execute actions"
```
Claude will call the `mcp_server.py` tool. The MCP Server will safely process the request and log the success into `mcp_server.log` to demonstrate external action capabilities without putting your actual social media accounts at risk of bans from botting!

---

## 🔒 Security & Privacy Notes
- **Mock MCP Mode:** Because LinkedIn explicitly bans headless browser bots, the MCP Server uses a safe "Mock" architecture that validates the Agentic flow perfectly while protecting your main social media accounts from restrictions. 
- **100% Local:** Everything occurs directly within the Obsidian vault. Data does not leave your local PC unless explicitly approved.

---
*Built for Hackathon 0 | Supreme Traders | 2026*

# 🤖 Personal AI Employee — Bronze Tier

> **Hackathon 0: Building Autonomous FTEs in 2026**
> *Your life and business on autopilot. Local-first, agent-driven, human-in-the-loop.*

---

## 📋 Tier Declaration
**BRONZE TIER** — Foundation (Minimum Viable AI Employee)

---

## 🏗️ Architecture Overview

```
External Input (File Drop)
        │
        ▼
┌──────────────────────┐
│  File System Watcher │  ← Python watchdog monitors /Inbox
│  (filesystem_watcher)│
└──────────┬───────────┘
           │ Creates .md files
           ▼
┌──────────────────────┐
│   Obsidian Vault     │  ← Local Markdown = Memory + Dashboard
│   /Needs_Action/     │
└──────────┬───────────┘
           │ Claude reads & processes
           ▼
┌──────────────────────┐
│     Claude Code      │  ← Reasoning Engine
│  + Agent Skills      │  ← process-vault-items skill
└──────────┬───────────┘
           │
    ┌──────┴──────┐
    ▼             ▼
/Plans/      /Pending_Approval/
(Plan.md)    (HITL approvals)
    │             │ Human approves
    └──────┬──────┘
           ▼
        /Done/
   + Dashboard.md updated
   + Logs/YYYY-MM-DD.json
```

---

## ✅ Bronze Tier Requirements Met

| Requirement | Status | Implementation |
|-------------|--------|----------------|
| Obsidian vault with Dashboard.md | ✅ | `AI_Employee_Vault/Dashboard.md` |
| Company_Handbook.md | ✅ | `AI_Employee_Vault/Company_Handbook.md` |
| One working Watcher script | ✅ | `src/filesystem_watcher.py` |
| Claude reads/writes to vault | ✅ | `CLAUDE.md` + agent skill |
| `/Inbox`, `/Needs_Action`, `/Done` folders | ✅ | Pre-created |
| All AI functionality as Agent Skills | ✅ | `.claude/skills/process-vault-items/` |

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.13+
- Node.js v24+ LTS
- [UV](https://docs.astral.sh/uv/) package manager
- Claude Code (`npm install -g @anthropic/claude-code`)

### 1. Install Dependencies
```powershell
# Install UV if not already installed
pip install uv

# Install all Python dependencies
uv sync
```

### 2. Configure Environment
```powershell
# The .env file is pre-created with safe defaults (DRY_RUN=true)
# To customize, edit .env
notepad .env
```

### 3. Run the AI Employee

**Option A — Orchestrator (recommended):**
```powershell
python src/orchestrator.py
```

**Option B — File Watcher only:**
```powershell
python src/filesystem_watcher.py
```

**Option C — Persistent (auto-restart):**
```powershell
python src/watchdog_process.py
```

### 4. Test It Works
```powershell
# Drop any file into the Inbox folder
echo "test invoice content" > "AI_Employee_Vault\Inbox\test_invoice.txt"

# Watch the Needs_Action folder — a .md file should appear within 5 seconds
ls "AI_Employee_Vault\Needs_Action\"
```

### 5. Use Claude Code to Process Items
```bash
# Open Claude Code in the project folder
claude

# Inside Claude Code, say:
# "Use the process-vault-items skill to check what's in Needs_Action"
```

---

## 📁 Project Structure

```
Bronze tier/
├── CLAUDE.md                          ← Claude Code instructions
├── pyproject.toml                     ← Python dependencies
├── .env                               ← Local config (DRY_RUN=true)
├── .env.example                       ← Template (safe to commit)
├── .gitignore
│
├── src/
│   ├── base_watcher.py               ← Abstract base class
│   ├── filesystem_watcher.py         ← ✅ Bronze Tier watcher
│   ├── gmail_watcher.py              ← Gmail watcher (needs OAuth)
│   ├── orchestrator.py               ← Master process
│   ├── watchdog_process.py           ← Health monitor
│   ├── audit_logger.py               ← JSON audit logging
│   └── retry_handler.py              ← Exponential backoff
│
├── .claude/
│   └── skills/
│       ├── process-vault-items/      ← ✅ Claude agent skill
│       │   └── SKILL.md
│       └── browsing-with-playwright/ ← Browser automation skill
│           └── SKILL.md
│
└── AI_Employee_Vault/
    ├── Dashboard.md                  ← ✅ Real-time status
    ├── Company_Handbook.md           ← ✅ Rules of engagement
    ├── Business_Goals.md             ← KPIs and targets
    ├── Inbox/                        ← Drop files here
    ├── Needs_Action/                 ← Watcher writes here
    ├── Done/                         ← Completed items
    ├── Plans/                        ← Claude's plan files
    ├── Pending_Approval/             ← HITL approval queue
    ├── Approved/                     ← Human-approved actions
    ├── Rejected/                     ← Human-rejected actions
    ├── Briefings/                    ← CEO briefings
    ├── Accounting/                   ← Financial data
    └── Logs/                         ← YYYY-MM-DD.json audit logs
```

---

## 🔒 Security

- **DRY_RUN=true** by default — no real external actions fire during development
- `.env` is in `.gitignore` — credentials never committed
- All actions logged to `/Logs/YYYY-MM-DD.json`
- Human-in-the-loop (HITL) for all sensitive actions
- Payments > $100 always require approval
- Emails to new contacts always require approval

### Credential Handling
- Credentials stored in `.env` (local only, never committed)
- Gmail OAuth token stored in `./credentials/` (in `.gitignore`)
- Use Windows Credential Manager for sensitive banking credentials

---

## 🎬 Demo Flow (for video recording)

1. Start the orchestrator: `python src/orchestrator.py`
2. Open Obsidian → `AI_Employee_Vault/` → observe Dashboard.md
3. Drop a file into `AI_Employee_Vault/Inbox/`
4. Watch `Needs_Action/` — a `.md` file appears automatically
5. Open Claude Code: `claude`
6. In Claude Code: *"Use the process-vault-items skill to process the inbox"*
7. Claude reads the file, creates a Plan.md, updates Dashboard.md
8. Show `Done/` folder — item moved there
9. Show `Logs/` — JSON audit trail

---

## 🗺️ Roadmap

| Tier | Features | Status |
|------|---------|--------|
| **Bronze** | Vault + File Watcher + Claude Skills | ✅ Complete |
| Silver | Gmail + LinkedIn + MCP Email Server | 🔜 Next |
| Gold | WhatsApp + Odoo + CEO Briefings | 🔜 Future |
| Platinum | Cloud deployment + always-on | 🔜 Future |

---

## 📚 Resources
- [Hackathon Guide](Personal%20AI%20Employee%20Hackathon%200-%20Building%20Autonomous%20FTEs%20in%202026%20(2).pdf)
- [Claude Code Docs](https://agentfactory.panaversity.org/docs/AI-Tool-Landscape/claude-code-features-and-workflows)
- [MCP Introduction](https://modelcontextprotocol.io/introduction)

---

*Built for Hackathon 0 | Ali Shahid

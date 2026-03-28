import time
import logging
from pathlib import Path
from datetime import datetime
import json
import random

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# This is a safe "Mock" Watcher that simulates receiving a new LinkedIn lead message
# without actually touching your real LinkedIn account.

MOCK_MESSAGES = [
    {"name": "Sarah Khan", "text": "Hi, I saw your recent post about Agentic AI. Are you available for a consulting project?"},
    {"name": "Ahmed Ali", "text": "Can you share your pricing for building a custom Digital FTE?"},
    {"name": "John Doe", "text": "Loved the hackathon project! Let's connect."}
]

def simulate_linkedin_notification():
    needs_action = Path('Needs_Action')
    needs_action.mkdir(exist_ok=True)
    
    msg = random.choice(MOCK_MESSAGES)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"LINKEDIN_MSG_{timestamp}.md"
    file_path = needs_action / file_name
    
    content = f"""---
type: linkedin_message
source: linkedin_watcher
sender: {msg['name']}
received: {datetime.now().isoformat()}
status: pending
---

# 🔗 New LinkedIn Message

**From:** {msg['name']}
**Message:** "{msg['text']}"

## Suggested Actions
- [ ] Draft a professional reply.
- [ ] Move to `Pending_Approval` so the human can review it before sending.
"""
    file_path.write_text(content, encoding='utf-8')
    logging.info(f"Simulated new LinkedIn message: {file_name}")

if __name__ == "__main__":
    logging.info("Starting safe LinkedIn Watcher (Mock Mode)...")
    logging.info("This will generate a fake LinkedIn message every 5 minutes for testing.")
    
    try:
        while True:
            # For demonstration, we trigger it every 300 seconds (5 mins)
            # You can change this to 60 for faster testing.
            time.sleep(300)
            simulate_linkedin_notification()
    except KeyboardInterrupt:
        logging.info("Stopping LinkedIn Watcher...")

import time
import logging
from pathlib import Path
from datetime import datetime

# Import our dashboard utility
try:
    from utils import update_dashboard
except ImportError:
    def update_dashboard():
        pass

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def trigger_marketing_post():
    vault_base = Path(__file__).parent.absolute()
    needs_action = vault_base / "Needs_Action"
    needs_action.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"TRIGGER_Marketing_{timestamp}.md"
    file_path = needs_action / file_name
    
    content = f"""---
type: scheduled_task
task: generate_linkedin_post
created: {datetime.now().isoformat()}
priority: high
status: pending
---

# ⏰ Scheduled Task: Marketing Post

It's time to generate your daily LinkedIn marketing post to drive sales!

## Instructions:
1. Review `Business_Goals.md` for current promo items.
2. Draft an engaging, professional LinkedIn post.
3. Save the crafted post to `Pending_Approval`.
4. Wait for the human to move it to `Approved` before doing anything else.
"""
    file_path.write_text(content, encoding='utf-8')
    logging.info(f"Generated scheduled trigger: {file_name}")
    # Update dashboard
    update_dashboard()

if __name__ == "__main__":
    logging.info("Starting Scheduler...")
    logging.info("Dashboard updates enabled.")
    
    # Initialize dashboard
    update_dashboard()
    
    # Trigger initial post for testing
    trigger_marketing_post()
    
    try:
        while True:
            # Check every hour or every minute for demo (let's keep 1 hour)
            time.sleep(3600)
            trigger_marketing_post()
    except KeyboardInterrupt:
        logging.info("Stopping Scheduler...")

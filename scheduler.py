import time
import logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def trigger_marketing_post():
    needs_action = Path('Needs_Action')
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
1. Review `Business_Goals.md` to see what we are currently promoting (e.g., our Digital FTE consulting services).
2. Draft an engaging, professional LinkedIn post.
3. Save the drafted post as a new file in the `Pending_Approval` folder using the format `APPROVAL_LINKEDIN_POST_<date>.md`.
4. Wait for the human to move it to `Approved` before doing anything else.
"""
    file_path.write_text(content, encoding='utf-8')
    logging.info(f"Generated scheduled trigger: {file_name}")

if __name__ == "__main__":
    logging.info("Starting Scheduler...")
    logging.info("Will generate a 'Marketing Post' trigger immediately, then every 1 hour.")
    
    trigger_marketing_post()
    
    try:
        while True:
            # For demonstration, wait 1 hour (3600 seconds)
            time.sleep(3600)
            trigger_marketing_post()
    except KeyboardInterrupt:
        logging.info("Stopping Scheduler...")

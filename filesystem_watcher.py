import time
import shutil
import logging
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Import our dashboard utility
try:
    from utils import update_dashboard
except ImportError:
    def update_dashboard():
        pass

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class WatcherHandler(FileSystemEventHandler):
    def __init__(self, vault_base):
        self.vault_base = Path(vault_base).absolute()
        self.inbox = self.vault_base / "Inbox"
        self.needs_action = self.vault_base / "Needs_Action"
        self.needs_action.mkdir(exist_ok=True)
        # Track processed files to avoid duplicates
        self.processed = set()

    def process_file(self, source):
        source = Path(source).absolute()
        if source.is_dir() or source.name.startswith('.') or source.name.startswith('~'):
            return
            
        if source.name in self.processed:
            return

        logging.info(f"Monitoring Inbox: Detected {source.name}")
        
        dest = self.needs_action / f"FILE_{source.name}"
        meta_path = self.needs_action / f"FILE_{source.name}.md"
        
        try:
            # Copy file
            shutil.copy2(source, dest)
            
            # Create MD metadata file
            content = f"""---
type: file_drop
original_name: {source.name}
received: {datetime.now().isoformat()}
status: pending
---

# New File: {source.name}

File dropped in Inbox for processing.

## Suggested Actions
- [ ] Review file content
- [ ] Take necessary action
"""
            meta_path.write_text(content, encoding='utf-8')
            logging.info(f"Created action file: {meta_path.name}")
            
            # Update Dashboard
            update_dashboard()
            self.processed.add(source.name)
            
        except Exception as e:
            logging.error(f"Error processing file: {e}")

    def on_created(self, event):
        self.process_file(event.src_path)

    def on_moved(self, event):
        self.process_file(event.dest_path)

if __name__ == "__main__":
    # Ensure all directories exist using absolute paths
    vault_base = Path(__file__).parent.absolute()
    inbox_path = vault_base / "Inbox"
    
    # Pre-create all folders
    for f in ["Inbox", "Needs_Action", "Done", "Plans", "Logs", "Skills"]:
        (vault_base / f).mkdir(exist_ok=True)
    
    event_handler = WatcherHandler(vault_base)
    observer = Observer()
    observer.schedule(event_handler, str(inbox_path), recursive=False)
    observer.start()
    
    logging.info(f"Watcher running on: {inbox_path}")
    logging.info("Polling fallback active (every 30s).")
    
    # Initial update
    update_dashboard()
    
    try:
        while True:
            time.sleep(1)
            # Polling fallback: Check Inbox every 30s just in case events are missed
            if int(time.time()) % 30 == 0:
                for item in inbox_path.iterdir():
                    if item.is_file():
                        event_handler.process_file(item)
    except KeyboardInterrupt:
        logging.info("Stopping watcher...")
        observer.stop()
    observer.join()

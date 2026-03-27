import time
import shutil
import logging
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class WatcherHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        source = Path(event.src_path)
        if source.name.startswith('.') or source.name.startswith('~'):
            return
            
        logging.info(f"Monitoring Inbox: Detected {source.name}")
        
        needs_action = Path('Needs_Action')
        needs_action.mkdir(exist_ok=True)
        
        dest = needs_action / f"FILE_{source.name}"
        
        try:
            # Copy file
            shutil.copy2(source, dest)
            
            # Create MD metadata file
            meta_path = needs_action / f"FILE_{source.name}.md"
            content = f"""---
type: file_drop
original_name: {source.name}
received: {datetime.now().isoformat()}
status: pending
---

# New File: {source.name}

File dropped for processing.

## Suggested Actions
- [ ] Review file content
- [ ] Take necessary action
"""
            meta_path.write_text(content, encoding='utf-8')
            logging.info(f"Created action file: {meta_path.name}")
            
        except Exception as e:
            logging.error(f"Error processing file: {e}")

if __name__ == "__main__":
    inbox_path = "Inbox"
    Path(inbox_path).mkdir(exist_ok=True)
    Path("Needs_Action").mkdir(exist_ok=True)
    Path("Done").mkdir(exist_ok=True)
    Path("Plans").mkdir(exist_ok=True)
    Path("Logs").mkdir(exist_ok=True)
    Path("Skills").mkdir(exist_ok=True)
    
    event_handler = WatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, inbox_path, recursive=False)
    observer.start()
    
    logging.info("Watcher running. Drop files in the Inbox folder to trigger.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Stopping watcher...")
        observer.stop()
    observer.join()

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def process():
    needs_action = Path('Needs_Action')
    if not needs_action.exists():
        logging.info("Needs_Action folder is empty.")
        return
        
    for item in needs_action.iterdir():
        if item.is_file() and item.suffix == '.md':
            logging.info(f"Processing action file: {item.name}")
            # Placeholder for processing logic
            
            # Move to Done
            done_folder = Path('Done')
            done_folder.mkdir(exist_ok=True)
            done_path = done_folder / item.name
            item.rename(done_path)
            logging.info(f"Moved {item.name} to Done.")

if __name__ == "__main__":
    logging.info("Starting processing Needs_Action items...")
    process()

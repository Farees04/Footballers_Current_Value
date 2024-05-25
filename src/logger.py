import logging
import os
from datetime import datetime

# Define temporary directory path (modify if needed)
TMP_DIR = "/tmp/logs"

# Create timestamped log filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Combine path and filename for log location
logs_path = os.path.join(TMP_DIR, LOG_FILE)

# Create the log directory with exist_ok=True to avoid errors if it exists
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
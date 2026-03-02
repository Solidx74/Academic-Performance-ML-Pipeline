import logging
import os
from datetime import datetime

# 1. Define the filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the 'logs' folder directory (Don't include the filename in the path yet!)
logs_path = os.path.join(os.getcwd(), "logs")

# 3. Create the directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# 4. Define the full path for the file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# 5. Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

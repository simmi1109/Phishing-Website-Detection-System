import logging
import os
from datetime import datetime

LOG_FILE= f"{datetime.now().strftime('%m-%d-%y %H-%M-%S')}.log" #this is the name of the log file, it will be created in the current directory
logs_path = os.path.join(os.getcwd(), 'logs',LOG_FILE) #this is the path to the logs directory, it will be created in the current directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True) #this will create the logs directory if it doesn't exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) #this is the full path to the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] - %(lineno)d %(name)s - %(message)s'
)

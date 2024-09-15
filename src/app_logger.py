import logging
import os

def setup_logger():
    """
    Set up logger for tracking app activities and errors.
    Logs will be save to `app.log`
    """
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    logger = logging.getLogger("TodoListApp")
    logger.setLevel(logging.INFO)

    log_file_path = os.path.join(log_directory, "app.log")
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

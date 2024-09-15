import pandas as pd 
from .exceptions import FileNotFoundError
from .app_logger import setup_logger


logger = setup_logger()

def load_tasks(file_path: str) -> pd.DataFrame:
    """
    Load task from csv file
    params:
        file_path: str - Path to the tasks csv file
    returns:
        pd.DataFrame: The task data
    """
    try:
        data = pd.read_csv(file_path)
        logger.info(f"Tasks loaded succesfully from {file_path}")
        return data
    except FileNotFoundError as e:
        logger.error(f"Failed to load tasks: {e}")
        raise FileNotFoundError

def save_tasks(data: pd.DataFrame, file_path: str):
    """
    Save task to csv file.
    params:
        data: pd.DataFrame - The task data.
        file_path: str - Path to the csv file.
    returns:
        None
    """
    data.to_csv("data/task.csv", index=False)
    logger.info(f"Task saved successfully to `{file_path}`")
    
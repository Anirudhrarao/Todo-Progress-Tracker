class TodoError(Exception):
    """
    Base class for all todo list related errors.
    """
    pass 

class FileNotFoundError(TodoError):
    """
    Exception raised when csv file is not found
    """
    def __init__(self, message="File not found. Please upload valid csv file."):
        self.message = message
        super().__init__(self.message)
    

class TaskAlreadyExistError(TodoError):
    """
    Exception raised when there are no task to display or process.
    """
    def __init__(self, message="Task already exists."):
        self.message = message
        super().__init__(self.message)

class NoTaskError(TodoError):
    """
    Exception raised when there are no tasks to display or process.
    """
    def __init__(self, message="No task found. Please add tasks first"):
        self.message = message
        super().__init__(self.message)

class NoDataError(TodoError):
    """
    Exception raised when data is none or empty
    """
    def __init__(self, message="Data is empty or none"):
        self.message = message
        super().__init__(self.message)
from .exceptions import TaskAlreadyExistError, NoTaskError
from .app_logger import setup_logger
from dataclasses import dataclass, field
import pandas as pd 

logger = setup_logger()

@dataclass
class TaskManager:
    task_df: pd.DataFrame = field(default_factory=lambda: pd.DataFrame(columns=['Task ID', 'Task Name', 'Category', 'Start Date', 'Due Date', 'Status', 'Priority', 'Progress', 'Completed']))

    def add_task(self, new_task: dict) -> None:
        """
        Add a new task to the task list.
        params:
            new_task: dict - New task details
        returns:
            None
        """
        if new_task in self.task_df.to_dict(orient='records'):
            raise TaskAlreadyExistError("This task is already in your to-do list.")
        else:
            new_task_id = self.task_df['Task ID'].max() + 1 if not self.task_df.empty else 1
            
            task_row = {
                "Task ID": new_task_id,
                "Task Name": new_task.get("Task Name", ""),
                "Category": new_task.get("Category", ""),  # Default or user input
                "Start Date": new_task.get("Start Date", ""),
                "Due Date": new_task.get("Due Date", ""),
                "Status": new_task.get("Status", "Not Started"),  # Default status
                "Priority": new_task.get("Priority", "Low"),  # Default priority
                "Progress": new_task.get("Progress", 0),  # Default 0 if not provided
                "Completed": new_task.get("Completed", False)  # Checkbox value
            }

            # Use pd.concat() instead of append (since append is deprecated)
            self.task_df = pd.concat([self.task_df, pd.DataFrame([task_row])], ignore_index=True)
            logger.info("New task added successfully.")
    
    def display_tasks(self) -> pd.DataFrame:
        """
        Display all tasks.
        returns:
            pd.DataFrame: Task DataFrame.
        """
        if self.task_df.empty:
            logger.warning("No tasks to display.")
            raise NoTaskError("No tasks available to display.")
        else:
            logger.info("Tasks displayed successfully")
            return self.task_df
    
    def mark_task_completed(self, task_name: str) -> None:
        """
        Mark a task as completed.
        params:
            task_name: str - The task name.
        returns:
            None.
        """
        task_filter = self.task_df["Task Name"] == task_name
        if not task_filter.any():  # Check if task exists
            logger.error(f"Task '{task_name}' not found.")
            raise TaskAlreadyExistError(f"Task '{task_name}' not found in the task list.")
        else:
            self.task_df.loc[task_filter, "Completed"] = True
            logger.info(f"Task `{task_name}` marked as completed.")
    
    def get_progress(self) -> float:
        """
        Calculate the overall progress as the average of the individual task progress percentages.
        returns:
            float: percentage of task completed.
        """
        if self.task_df.empty:
            logger.warning("No tasks available to calculate progress.")
            return 0.0
        
        # Ensure 'Progress' column is numeric and handle NaN or invalid entries
        self.task_df['Progress'] = pd.to_numeric(self.task_df['Progress'], errors='coerce').fillna(0)
        
        # Calculate the average progress
        total_progress = self.task_df['Progress'].sum()
        num_tasks = len(self.task_df)
        
        if num_tasks == 0:
            return 0.0
        
        average_progress = total_progress / num_tasks
        logger.info(f"Task progress calculated: {average_progress}%")
        return average_progress


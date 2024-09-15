# Personal To-Do List Tracker

A web-based personal to-do list tracker built with Streamlit, allowing users to manage and track their tasks, view progress, and mark tasks as completed. 

## Features

- **Add New Tasks**: Users can add tasks with details such as task name, category, start date, due date, status, priority, progress, and whether the task is completed.
- **Task Visualization**: Displays tasks in a table with real-time updates.
- **Mark Tasks as Completed**: Allows users to mark tasks as completed.
- **Track Overall Progress**: Shows the overall progress of tasks with a progress bar.
- **Data Persistence**: Tasks are stored in a CSV file to ensure persistence across sessions.

## Project Structure

```bash
📁 project-root/
│
├── 📁 src/
│   ├── task_manager.py        # Handles task-related operations
│   ├── file_handler.py        # Functions to load and save tasks
│   ├── app_logger.py          # Logger setup for the application
│   ├── visualizer.py          # Data visualization for tasks
│   └── exceptions.py          # Custom exceptions for task operations
│
├── data/
│   └── tasks.csv              # CSV file storing the task data
│
├── app.py                     # Main Streamlit app entry point
└── README.md                  # Project documentation

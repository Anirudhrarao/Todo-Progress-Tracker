import streamlit as st 
from src.task_manager import TaskManager
from src.file_handler import load_tasks, save_tasks
from src.app_logger import setup_logger
from src.exceptions import NoTaskError, TaskAlreadyExistError
from src.visualizer import Visualizer

logger = setup_logger()

def main():
    st.title("Personal To-Do List Tracker")

    try:
        # Reading and displaying data 
        task_df = load_tasks("data/task.csv")  
        task_manager = TaskManager(task_df)
        visualizer = Visualizer(task_df)

        st.subheader("Task List")
        try:
            if not task_manager.task_df.empty:
                st.dataframe(task_manager.display_tasks())
            else:
                st.warning("No tasks to display.")
        except NoTaskError as e:
            st.warning(str(e))
            logger.error(f"Display tasks failed: {e}")
        
        # Visualize the data
        visualizer.visualize_data()

        # Adding new task in the dataframe
        with st.form("Add New Task"):
            task_name = st.text_input("Task Name") 
            category = st.text_input("Category")  # Optional input
            start_date = st.date_input("Start Date")
            due_date = st.date_input("Due Date")
            status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
            priority = st.selectbox("Priority", ["Low", "Medium", "High"])
            progress = st.slider("Progress", 0, 100, 0)
            completed = st.checkbox("Completed")
            submit_task = st.form_submit_button("Add Task")

            if submit_task:
                new_task = {
                    "Task Name": task_name,
                    "Category": category,
                    "Start Date": start_date,
                    "Due Date": due_date,
                    "Status": status,
                    "Priority": priority,
                    "Progress": progress,
                    "Completed": completed
                }

                try:
                    task_manager.add_task(new_task)
                    save_tasks(task_manager.task_df, "data/tasks.csv")
                    st.success("New task added successfully!")
                except TaskAlreadyExistError as e:
                    st.warning(str(e))
                
        # Mark task as completed
        st.subheader("Mark Task as Completed")
        task_to_mark = st.text_input("Task Name to Mark as Completed")
        if st.button("Mark as Completed"):
            try:
                task_manager.mark_task_completed(task_to_mark)
                save_tasks(task_manager.task_df, "data/tasks.csv")
                st.success(f"Task '{task_to_mark}' marked as completed!")
            except TaskAlreadyExistError as e:
                st.warning(str(e))
            
        # Show progress
        st.subheader("Task Progress")
        progress = task_manager.get_progress()  
        st.progress(progress / 100) 
        st.text(f"Overall Progress: {progress:.2f}%")

    except FileNotFoundError as e:
        st.error(str(e))
        logger.error(f"Application error: {e}")

if __name__ == "__main__":
    main()

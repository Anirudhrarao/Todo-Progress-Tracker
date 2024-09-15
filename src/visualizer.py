import streamlit as st
import plotly.express as px
from src.app_logger import setup_logger
from src.exceptions import NoDataError
import pandas as pd
from dataclasses import dataclass

logger = setup_logger()

@dataclass
class Visualizer:
    data: pd.DataFrame = None

    def load_data(self, file_path: str):
        """
        Load data from a given file path and set it as an instance variable.
        """
        try:
            self.data = pd.read_csv(file_path)
            logger.info(f"Data loaded successfully from {file_path}.")
        except Exception as e:
            logger.error(f"Failed to load data from {file_path}: {e}")
            st.error(f"Failed to load data from {file_path}. Please check the file and try again.")

    def visualize_data(self):
        """
        Visualize the data using bar and pie charts.
        """
        try:
            if self.data is not None:
                # Ensure that required columns exist
                required_columns = ['Priority', 'Status']
                if not all(col in self.data.columns for col in required_columns):
                    raise NoDataError(f"Required columns {required_columns} are missing in the data.")

                st.subheader("Task Breakdown by Priority")
                priority_task_count = self.data['Priority'].value_counts()
                st.bar_chart(priority_task_count)

                st.subheader("Completion Status Breakdown")
                completion_status = self.data['Status'].value_counts()

                fig = px.pie(
                    values=completion_status,
                    names=completion_status.index,
                    title="Task Completion Status"
                )
                st.plotly_chart(fig)
                logger.info("Data visualized successfully.")
            else:
                raise NoDataError("No data available to visualize.")
        except NoDataError as e:
            st.warning(str(e))
            logger.error(f"Data visualization failed: {e}")

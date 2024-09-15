from setuptools import setup, find_packages

setup(
    name='todo_progress_tracker',  
    version='0.1.0',
    packages=find_packages(), 
    include_package_data=True,
    install_requires=[
        'streamlit',
        'pandas',
        'plotly', 
    ]
)

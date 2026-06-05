import streamlit as st
import pandas as pd

# Page conf
st.set_page_config(page_title="Task Checker", page_icon=":pictures/clipboard.png:", layout="centered")
# Title
st.title("Task Checker")
# File uploader
uploaded_file = st.file_uploader("Upload your task file (CSV format)", type=["csv"])
if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    # Display the DataFrame
    st.write("Uploaded Task Data:")
    st.dataframe(df)
    # Check for missing values
    if df.isnull().values.any():
        st.warning("There are missing values in the task data. Please check your file.")
    else:
        st.success("All tasks are complete! No missing values found.")
        

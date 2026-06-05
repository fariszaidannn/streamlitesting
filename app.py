import streamlit as st
import pandas as pd

# Page conf
st.set_page_config(page_title="Task Checker", page_icon=":pictures/clipboard.png:", layout="centered")

# Title > HTML
st.title("Task Checker")
st.markdown(
    """
    <div class="app-header">
    <h1> Task Checker </h1>
    <p> This is a simple task checker app built with Streamlit. </p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Conditions
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"text": "Open streamlit account", "done": True},
        {"text": "Create a task checker app", "done": True}
    ]
    
# Style > CSS
st.markdown(
    """
    <style>
    .app-header{
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    
    """
    , unsafe_allow_html=True
)

# Add task
col_inp, col_btn = st.columns([3, 1])
with col_inp:
    task_text = st.text_input("Add a new task", 
                              placeholder="Enter task description...", 
                              label_visibility="collapsed")
with col_btn:
    if st.button("Add", use_container_width=True):
        if task_text.strip():
            st.session_state.tasks.append({"text": task_text.strip(), "done": False})
            st.success("Task added!")
        else:
            st.error("Please enter a task description.")
            
        st.rerun()
st.write("")

# Task list
if not st.session_state.tasks:
    st.info("No tasks added yet. Please add a task to get started.")

for i, task in enumerate(st.session_state.tasks):
    c1, c2, c3 = st.columns([0.1, 0.8, 0.1])
    with c1:
        # Removed use_container_width=True from the checkbox below
        checked = st.checkbox("", value=task["done"], key=f"chk_{i}",
                              label_visibility="collapsed")
        if checked != task["done"]:
            st.session_state.tasks[i]["done"] = checked
            st.rerun()
    with c2:
        st.write(task["text"])
    with c3:
        if st.button("Delete", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()
            

# Summary
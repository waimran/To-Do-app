import streamlit as st

def add_task(tasks, task):
    tasks.append(task)
    return tasks

def view_tasks(tasks):
    for task in tasks:
        st.write(task)

st.title("Todo App")
tasks = []

task = st.text_input("Task")
if st.button("Add Task"):
    tasks = add_task(tasks, task)

view_tasks(tasks)
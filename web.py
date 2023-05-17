import streamlit as st
import functions
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

todos = functions.get_todos()


def add_todo():
    todo_new = st.session_state["new_todo"] + '\n'
    todos.append(todo_new)
    functions.set_todos(todos)


st.title("My To-Do App")
st.subheader("This is my to-do Web App")
st.write("This app is used to increase your <b>productivity</b>", unsafe_allow_html=True)


st.text_input(label="", placeholder="Add a Todo......",
              on_change=add_todo,
              key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index).strip('\n')
        functions.set_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


# label is used to display the text just above the text box
# while placeholder is used to display the bydefault text in text box
st.session_state

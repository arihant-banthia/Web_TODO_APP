import streamlit as st
import functions

todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("This is my to-do wen App")
st.write("This app is used to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a Todo......")
# label is used to display the text just above the text box
# while placeholder is used to display the bydefault text in text box

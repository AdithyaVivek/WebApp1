from turtle import onclick

import streamlit as st
import functions

todos = functions.get_todos()


st.set_page_config(layout="wide")
st.session_state["textbox_new_todo"] = ""

def add():
    new_todo = st.session_state["textbox_new_todo"] + "\n"
    if todos.__contains__(new_todo):
        st.info("Todo exists.. Finish it")
    else:
        todos.append(new_todo)
        functions.put_todos(todos)

        print(todos)


st.title("My Todo App")
st.header("This is my todo App")
st.subheader("This is my todo App")
st.write("This app increase your <b><u>productivity</u></b>",
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.put_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


add = st.text_input(label="textbox_new_todo", label_visibility="hidden", placeholder="Enter a todo", on_change=add,
                    key="textbox_new_todo")




# st.session_state

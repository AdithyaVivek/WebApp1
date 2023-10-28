import streamlit as st
import functions

todos = functions.get_todos()


def add():
    new_todo = st.session_state["textbox_new_todo"] + "\n"
    todos.append(new_todo)
    functions.put_todos(todos)
    print(todos)


st.title("My Todo App")
st.header("This is my todo App")
st.write("This app increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.put_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="new_todo", label_visibility="hidden", placeholder="Enter a todo", on_change=add,
              key="textbox_new_todo")

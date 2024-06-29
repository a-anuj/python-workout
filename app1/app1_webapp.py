import streamlit as st
import functions_app1

todos = functions_app1.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions_app1.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("To-Do App")
st.subheader("A Web-App to keep an eye on your "
             "todo list  ")

st.text_input("", placeholder="Enter todo..."
              , on_change=add_todo, key="new_todo")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions_app1.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()



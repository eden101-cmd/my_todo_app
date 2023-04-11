#creating web app
#we need to run it only in the terminal! ->
# write: cd important and after it streamlit run web.py
import streamlit as st #easy to creating web apps, integrate good with graphs
import functions_for_app

todos = functions_for_app.get_todos()

#the add to the todos
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions_for_app.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app will be used to increase your productivity.")
#the order matters!

#amnaging the todos list
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo) #סימון וי על אופציות
    if checkbox:
        todos.pop(index)
        functions_for_app.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')


# st.session_state = looks like a dictionary but not exactly: the new_todo is the key
#and what we will enter will be used as the value of this "key"
#st.text_input -> the first argument is a little title to the text box.

# placeholder it whar we will be written to the user in the checkbox
# what we will enter will be a new_todo
#the add_todo function will be the connection between the todos to the web app.
#new_todo will be the key that mentioned in the function of the add_todo.
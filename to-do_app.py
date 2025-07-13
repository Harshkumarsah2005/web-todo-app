import streamlit as st
import functions
st.title("MY TO-DO APP")
st.subheader("First web page")
st.write("this is to improve my productivity")

todos= functions.get_todo( )

def add_todo( ):
    to_do= st.session_state['new_todo']
    todos.append(to_do)
    functions.write_todo(todos)

for todo in todos:
    st.checkbox(todo)

st.text_input("enter a new to-do:- ", placeholder="write your task", on_change= add_todo, key='new_todo')

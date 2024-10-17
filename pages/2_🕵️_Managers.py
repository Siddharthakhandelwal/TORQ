import streamlit as st
import database_ware as dbb

from streamlit_option_menu import option_menu


st.set_page_config(
    page_title='TORQ', 
    layout='wide',
    page_icon="🐦"               
)
st.snow()
st.sidebar.title("WAREHOUSE MANAGEMENT SYSTEM")

st.image("DATA TAKES FLIGHT.png", use_column_width=True)

# Page Setup 
#Image In Sidebar 
with st.sidebar.container(): 
    st.image('1.png', use_column_width=True, caption='TORQ : DATA TAKES FLIGHT')
st.sidebar.markdown("---")

def print_praise():
    praise_quotes = """
    Keshav Agrawal
    Archi Agrawal
    Siddhartha Khandelwal
    Nimit Goyal
    Pragati Agrawal
    Uday Chauhan
    """
    title = "**Brought to you By -**\n\n"
    return title + praise_quotes

st.sidebar.success(print_praise())   
st.sidebar.write("---\n")
st.sidebar.info("Special Thanks to our Mentor\n\nDr.Neeraj Gupta Sir, Faculty, DBMS\n\nGLA UNIVERSITY, MATHURA")

st.header("Managers")
#tabs
def streamlit_menu():
    selected = option_menu(
        menu_title='Manager',  # required
        options=["New Manager", "Delete Manager Record"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected

selected = streamlit_menu()
if selected == "New Manager":
    col1,col2,col3,col4 =  st.columns([2,2,2,2])
    with col1:
        a=st.text_input("Manager ID")

    create=st.button("Create")
    if a and create:
        dbb.mana_insert(a)
        st.success("Manager is inserted") 
    else: 
        st.error("Please enter Valid ID")
            
if selected =="Delete Manager Record":
    a=st.text_input("ID")
    b=st.button("Delete")
    if b:
        if dbb.man_del(a):
            st.success(f"Manager with id {a} is deleted")
        else:
            st.error("Error deleting manager")

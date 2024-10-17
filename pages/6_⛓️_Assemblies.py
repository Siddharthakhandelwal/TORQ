import streamlit as st
from streamlit_option_menu import option_menu
import database_ware as dbb
import pandas as pd
import sqlite3

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

st.header("Assemblies")
#tabs
def streamlit_menu():
    selected = option_menu(
        menu_title='Assemblies',  # required
        options=["New Assemblies", "Delete Assemblies Record"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected

selected = streamlit_menu()
if selected=="New Assemblies":
    col1,col2,col3,col4 =  st.columns([2,2,2,2])
    with col1:
        q=st.text_input("Assembly ID")
# check conditions 
    create=st.button("Create")
    if  col1 and col2 and create:
        dbb.ass_insert(q)
        st.success(f"Assembly ID {q} has been inserted")
    else:
        pass

    
if selected=="Delete Assemblies Record":
    try:
        a=st.text_input("Assembly ID")
        Dele=st.button("Delete")
        if Dele:
            
            dbb.ass_del(a)
            st.success(f"Assembly id {a} has been deleted")
    except:
        st.error("Enter valid Id or create one")

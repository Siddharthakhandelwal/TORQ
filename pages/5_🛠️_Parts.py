import streamlit as st
from streamlit_option_menu import option_menu
import database_ware as dbb
import sqlite3
import pandas as pd

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

st.header("Parts")
#tabs
def streamlit_menu():
    selected = option_menu(
        menu_title='Parts',  # required
        options=["New Part", "Update Part Details", "Delete Part Record"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected

selected = streamlit_menu()
if selected=="New Part":
    col1,col2,col3,col4 =  st.columns([2,2,2,2])
    with col1:
        q=st.text_input("Part Number")
    with col2:
        w=st.text_input("Assembly ID")
# check conditions 
    create=st.button("Create")
    if  col1 and col2 and create:
        dbb.part_insert(q,w)
        st.success("Following Data is inserted")
        data=dbb.update_part(q)
        df = pd.DataFrame([data], columns=['Part Number', 'Assembly ID'])
        st.write(df)
    else:
        pass
        
        
if selected=="Update Part Details":
    try:
        q=st.text_input("Part ID")
        find_part=st.button("FIND")
        if dbb.update_part(q) is not None:
            data=dbb.update_part(q)
            df = pd.DataFrame([data], columns=['Part Number', 'Assembly ID'])

            col1,col2,col3,col4 =  st.columns([2,2,2,2])
        with col1:
            w=st.text_input("Assembly ID",value=data[1])
            
        create=st.button("Update")
        if  col1 and create:
            st.markdown("Here is previous data")
            st.write(df)
            query = """UPDATE Parts 
                SET assembly_id=?
                WHERE  part_number= ?"""
            data = (w, q)
            
            connection = sqlite3.connect("warehouse.db")
            cursor = connection.cursor()
            cursor.execute(query, data)
            connection.commit()
            st.write("Updated data is")
            data=dbb.update_part(q)
            df = pd.DataFrame([data], columns=['Part Number', 'Assembly ID'])
            st.write(df)
            st.success("Data has been updated")
    except:
        st.error("Enter Valid Id or create one")
        
    
if selected=="Delete Part Record":
    try:
        a=st.text_input("Part ID")
        del_part=st.button("Delete")
        if del_part:
            data=dbb.update_part(a)
            dbb.parts_del(a)
            df = pd.DataFrame([data], columns=['Part Number', 'Assembly ID'])
            st.success("Following data has been deleted")
            st.write(df)
            
    except:
        st.error("Enter Valid Id or create one")
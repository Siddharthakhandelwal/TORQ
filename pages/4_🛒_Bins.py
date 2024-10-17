import streamlit as st
import database_ware as dbb
import pandas as pd
import sqlite3
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

st.header("Bin")
def streamlit_menu():
    selected = option_menu(
        menu_title='Bin',  # required
        options=["New Bin", "Update Bin Details", "Delete Bin"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected

selected = streamlit_menu()
if selected=="New Bin":
    col1,col2,col3=  st.columns([2,2,2])
    with col1:
        q=st.text_input("Bin Number")
    with col2:
        w=st.text_input("Ware House ID")
    with col3:
        r=st.text_input("Capacity")
        
    create=st.button("Create")
    if  col1 and col2 and col3  and create:
        dbb.bin_insert(q,w,r)
        data=dbb.update_bin(q)
        df = pd.DataFrame([data], columns=['Bin Number', 'Warehouse ID', 'Capacity'])
        st.write("The follwing data is Inserted")
        st.write(df)
    else:
        pass
        
        
if selected =="Update Bin Details":
    try:
        bin_id=st.text_input("Bin ID")
        find_bin=st.button("Find")
        if dbb.update_bin(bin_id) is not None:
            data=dbb.update_bin(bin_id)
            df = pd.DataFrame([data], columns=['Bin Number', 'Warehouse ID', 'Capacity'])
        
            col1,col2,col3=  st.columns([2,2,2])
        with col1:
            w=st.text_input("Ware House ID",value=data[1])
        with col2:
            r=st.text_input("Capacity",value=data[2])
            
        create=st.button("Update")
        if  col1 and col2 and create:
            st.markdown("Here is previous data")
            st.write(df)
            query = """UPDATE Bins 
                SET warehouse_id=?,capacity=?
                WHERE bin_number = ?"""
            data = (w,r,bin_id)
            
            connection = sqlite3.connect("warehouse.db")
            cursor = connection.cursor()
            cursor.execute(query, data)
            connection.commit()
            st.write("Updated data is")
            data=dbb.update_bin(bin_id)
            df = pd.DataFrame([data], columns=['Bin Number', 'Warehouse ID', 'Capacity'])
            st.write(df)
    except:
        st.error("Enter Valid ID or Create One")
        
if selected =="Delete Bin":
    try:
        bin_id=st.text_input("Bin ID")
        del_bin=st.button("Delete")
        if del_bin:
            data=dbb.update_bin(bin_id)
            df = pd.DataFrame([data], columns=['Bin Number', 'Warehouse ID', 'Capacity'])
            st.success("Following data is deleted")
            st.write(df)
            dbb.bin_del(bin_id)
            
    except:
        st.error("Enter Valid ID or Create One")


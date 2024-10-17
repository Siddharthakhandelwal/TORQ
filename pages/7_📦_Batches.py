import streamlit as st
import database_ware as dbb
from streamlit_option_menu import option_menu
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

st.header("Batches")
#tabs
def streamlit_menu():
    selected = option_menu(
        menu_title='Batches',  # required
        options=["New Batches", "Update Batches Details", "Delete Batches Record"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected

selected = streamlit_menu()
if  selected == "New Batches":
    col1,col2,col3,col4 =  st.columns([2,2,2,2])
    col5,col6,col7=st.columns([2,2,2])
    with col1:
        a=st.text_input("Batch Number")
    with col2:
        b=st.text_input("Part Number")
    with col3:
        w=st.text_input("Date In")
    with col5:
        e=st.text_input("Size")
    with col6:
        r=st.text_input("Bin Number")
    with col7:
        t=st.text_input("Manager ID")
    
# check conditions 
    create=st.button("Create")
    if col1 and col2 and col3 and col4 and col5 and col6 and col7 and create:
        dbb.batch_insert(a,b,w,e,r,t)
        batch_data=dbb.update_batch(a)
        df = pd.DataFrame([batch_data], columns=['Batch Number', 'Part Number', 'Date In', 'Size', 'Bin Number', 'Manager ID'])
        st.success("Following data has been inserted")
        st.write(df)
    else:
        pass
        


if  selected == "Update Batches Details":
    try:
        a=st.text_input("ID")
        st.button("Find")
        if dbb.update_batch(a) is not None:
            batch_data=dbb.update_batch(a)
            df = pd.DataFrame([batch_data], columns=['Batch Number', 'Part Number', 'Date In', 'Size', 'Bin Number', 'Manager ID'])

            col2,col3,col4 =  st.columns([2,2,2])
            col5,col6,col7=st.columns([2,2,2])
            
            with col2:
                b=st.text_input("Part Number",batch_data[1])
            with col3:
                w=st.text_input("Date In",batch_data[2])
            with col5:
                e=st.text_input("Size",batch_data[2])
            with col6:
                r=st.text_input("Bin Number",batch_data[3])
            with col7:
                t=st.text_input("Manager ID",batch_data[4])
            upodate=st.button("Update")
            if col2 and col3 and col4 and col5 and col6 and col7 and upodate:
                st.markdown("Here is previous data")
                st.write(df)
                query = """UPDATE Batches
                SET part_number=?, date_in=?, size=?, bin_number=?, manager_id=?
                WHERE batch_number = ?"""
                data = (b,w,e,r,t,a)
                
                connection = sqlite3.connect("warehouse.db")
                cursor = connection.cursor()
                cursor.execute(query, data)
                connection.commit()
                st.write("Updated data is")
                batch_data=dbb.update_batch(a)
                df = pd.DataFrame([batch_data], columns=['Batch Number', 'Part Number', 'Date In', 'Size', 'Bin Number', 'Manager ID'])
                st.write(df)
                st.success("Data has been updated sucessfully")
        else:
            st.error("no data found")
    except:
        st.error("Enter Valid ID or Create one")

if selected == "Delete Batches Record":
    try:
        a=st.text_input("ID")
        delo=st.button("Delete")
        if delo:
            batch_data=dbb.update_batch(a)
            df = pd.DataFrame([batch_data], columns=['Batch Number', 'Part Number', 'Date In', 'Size', 'Bin Number', 'Manager ID'])
            dbb.batches_del(a)
            st.success("Following data has been deleted")
            st.write(df)
    except:
        st.error("Enter valid Id or create One")
        

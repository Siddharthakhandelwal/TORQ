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

st.header("Backorders")
#tabs
def streamlit_menu():
    selected = option_menu(
        menu_title='Backorders',  # required
        options=["New Backorders", "Update Backorders Details", "Delete Backorders Record"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected

selected = streamlit_menu()
if  selected == "New Backorders":
    col1,col2,col3,col4 =  st.columns([2,2,2,2])
    col5,col6=st.columns([2,2])
    with col1:
        a=st.text_input("Backorder ID")
    with col2:
        b=st.text_input("Part Number")
    with col3:
        c=st.text_input("Manager ID")
    with col4:
        d=st.text_input("Date backordered")
    with col5:
        e=st.text_input("Quantity Backordered")
    with col6:
        f=st.text_input("Remainig Quantity")
        
# check conditions 
    create=st.button("Create")
    if  col1 and col2 and col3 and col4 and col5 and col6  and create:
        dbb.back_insert(a,b,c,d,e,f)
        st.success("Following data has been inserted")
        backorder_data=dbb.update_backorder(a)
        df = pd.DataFrame([backorder_data], columns=['Backorder ID', 'Part Number', 'Manager ID', 'Date Backordered', 'Quantity Backordered', 'Remaining Quantity'])
        st.write(df)
    else:
        pass

#IDK what to do
if  selected == "Update Backorders Details":
    try:
        a=st.text_input("ID")
        st.button("Find")
        if dbb.update_backorder is not None:
            backorder_data=dbb.update_backorder(a)
            df = pd.DataFrame([backorder_data], columns=['Backorder ID', 'Part Number', 'Manager ID', 'Date Backordered', 'Quantity Backordered', 'Remaining Quantity'])
            col2,col3,col4 =  st.columns([2,2,2])
            col5,col6=st.columns([2,2])
            with col2:
                b=st.text_input("Part Number",backorder_data[1])
            with col3:
                c=st.text_input("Manager ID",backorder_data[2])
            with col4:
                d=st.text_input("Date backordered",backorder_data[3])
            with col5:
                e=st.text_input("Quantity Backordered",backorder_data[4])
            with col6:
                f=st.text_input("Remainig Quantity",backorder_data[5])
            update=st.button("Update")
            if col2 and col3 and col4 and col5 and col6 and update:
                st.markdown("Here is previous data")
                st.write(df)
                query = """UPDATE Backorders 
                SET part_number=?, manager_id=?, date_backordered=?, quantity_backordered=?, remaining_quantity=?  WHERE backorder_id = ?"""
                data = (b,c,d,e,f,a)
                
                connection = sqlite3.connect("warehouse.db")
                cursor = connection.cursor()
                cursor.execute(query, data)
                connection.commit()
                st.write("Updated data is")
                backorder_data=dbb.update_backorder(a)
                df = pd.DataFrame([backorder_data], columns=['Backorder ID', 'Part Number', 'Manager ID', 'Date Backordered', 'Quantity Backordered', 'Remaining Quantity'])
                st.write(df)
                st.success("Data has been updated")
        else:
            st.error("no data found")
    except:
        st.error("Enter Valid ID or Create one")

        

if selected == "Delete Backorders Record":
    try:
        a=st.text_input("ID")
        dolo=st.button("Delete")
        if dolo:
            backorder_data=dbb.update_backorder(a)
            df = pd.DataFrame([backorder_data], columns=['Backorder ID', 'Part Number', 'Manager ID', 'Date Backordered', 'Quantity Backordered', 'Remaining Quantity'])
            dbb.back_del(a)
            st.success("Data has been deleted")
            st.write(df)
    except:
        st.error("Enter Valid Id or Create One")
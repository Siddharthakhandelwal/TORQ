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

st.header("Ware House")

def streamlit_menu():
    selected = option_menu(
        menu_title='Ware House',  # required
        options=["New Ware House", "Update Ware House Details", "Delete Ware House Record"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected

selected = streamlit_menu()
#tabs
if selected =="New Ware House":
    col1,col2 =  st.columns([2,2])
    with col1:
        q=st.text_input("Ware House  ID")
    with col2:
        w=st.text_input("ware House Symbol") 
    create=st.button("Create")
    
    if col1 and col2 and create:
        dbb.war_insert(q,w)    
        st.write("The following data is Inserted")
        data=dbb.update_warehouse(q)
        df = pd.DataFrame([data], columns=['Warehouse ID', 'Warehouse Symbol'])
        st.write(df)
        st.success("Data is Inserted Succesfully")
        
    else:
        pass
        

if selected =="Update Ware House Details":
    try:
        A=st.text_input("ID")
        Find=st.button("Find")
        if dbb.update_warehouse(A) is not None:
            data=dbb.update_warehouse(A)
            df = pd.DataFrame([data], columns=['Warehouse ID', 'Warehouse Symbol'])
            st.write(df)
            col1,col2 =  st.columns([2,2])
            with col1:
                w=st.text_input("ware House Symbol",value=data[1]) 
            create=st.button("Update")
            
            if col1  and create:
                st.markdown("Here is previous data")
                st.write(df)
                query = """UPDATE Warehouses 
                SET  warehouse_symbol = ?
                WHERE  warehouse_id= ?"""
                data = (w,A)
                
                connection = sqlite3.connect("warehouse.db")
                cursor = connection.cursor()
                cursor.execute(query, data)
                connection.commit()
                st.write("Updated data is")
                data=dbb.update_warehouse(A)
                df = pd.DataFrame([data], columns=['Warehouse ID', 'Warehouse Symbol'])
                st.write(df)
        else:
            st.error("no data found")
    except:
        st.error("Enter Valid Id or create one")
        
if selected == "Delete Ware House Record":
    try:
        A=st.text_input("ID")
        delete=st.button("Delete")
        if delete:
            data=dbb.update_warehouse(A)
            df = pd.DataFrame([data], columns=['Warehouse ID', 'Warehouse Symbol'])
            st.write("The following data is deleted")
            st.write(df)
            dbb.ware_del(A)
    except:
        st.error("Enter Valid ID or Create One")
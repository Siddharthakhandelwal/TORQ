import streamlit as st
import database_ware as dbb
import sqlite3
import pandas as pd
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

st.header("Shipments")
#tabs
def streamlit_menu():
    selected = option_menu(
        menu_title='Employees',  # required
        options=["New Shipments", "Update Shipments Details", "Delete Shipments Record"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected

selected = streamlit_menu()
if  selected == "New Shipments":
    col1,col2,col3,col4 =  st.columns([2,2,2,2])

    with col1:
        q=st.text_input("Shipment ID")
    with col2:
        w=st.text_input("Batch Number")
    with col3:
        e=st.text_input("Date Out")
    with col4:
        r=st.text_input("Employee ID")  
    
# check conditions 
    create=st.button("Create")
    if  col1 and col2 and col3 and col4 and create:
        dbb.ship_insert(q,w,e,r)
        shipment_data=dbb.update_shipment(q)
        df = pd.DataFrame([shipment_data], columns=['Shipment ID', 'Batch Number', 'Date Out', 'Employee ID'])
        st.write(df)
        st.success("Following data has been added")
    else:
        pass


if  selected == "Update Shipments Details":
    try:
        a=st.text_input("ID")
        st.button("Find")
        if dbb.update_shipment(a) is not None:
            shipment_data=dbb.update_shipment(a)
            df = pd.DataFrame([shipment_data], columns=['Shipment ID', 'Batch Number', 'Date Out', 'Employee ID'])
            col1,col2,col3,col4 =  st.columns([2,2,2,2])
            with col1:
                w=st.text_input("Batch Number",value=shipment_data[1])
            with col2:
                e=st.text_input("Date Out",value=shipment_data[2])
            with col3:
                r=st.text_input("Employee ID",value=shipment_data[3])  
            
        # check conditions 
            create=st.button("Update")
            if  col1 and col2 and col3 and create:
                st.markdown("Here is previous data")
                st.write(df)
                query = """UPDATE Shipments 
                SET batch_number=?, date_out=?, employee_id=? WHERE shipment_id = ?"""
                data = (w,e,r,a)
                
                connection = sqlite3.connect("warehouse.db")
                cursor = connection.cursor()
                cursor.execute(query, data)
                connection.commit()
                st.write("Updated data is")
                data=dbb.update_shipment(a)
                df = pd.DataFrame([shipment_data], columns=['Shipment ID', 'Batch Number', 'Date Out', 'Employee ID'])
                st.write(df)
                st.success("Data has been updated")
        else:
            st.error("no data found")
    except:
        st.error("Enter Valid ID or create one")
            
        
    

if selected == "Delete Shipments Record":
    try:
        a=st.text_input("ID")
        delo=st.button("Delete")
        if delo:
            
            shipment_data=dbb.update_shipment(a)
            df = pd.DataFrame([shipment_data], columns=['Shipment ID', 'Batch Number', 'Date Out', 'Employee ID'])
            dbb.ship_del(a)
            st.write(df)
            st.success("Data has been deleted")
    except:
        st.error("Enter Valid ID or create one")

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
# st.snow()
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

st.header("Employees")

def streamlit_menu():
    selected = option_menu(
        menu_title='Employees',  # required
        options=["New Employee", "Update Employee Details", "Delete Employee Record"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected

selected = streamlit_menu()
if  selected == "New Employee":
    col1,col2,col3,col4,col5 =  st.columns([2,2,2,2,2])
    col6,col7,col8,col9,col10=st.columns([2,5,2,2,2])
    with col1:
        q=st.text_input("Employee ID")
    with col2:
        w=st.text_input("Phone Number")
    with col3:
        e=st.text_input("First Name")
    with col4:
        r=st.text_input("Middle Name")
    with col5:
        t=st.text_input("Last Name")
    with col6:
        y=st.text_input("Street Number")
    with col7:
        u=st.text_input("Street Name")
    with col8:
        i=st.text_input("City")
    with col9:
        o=st.text_input("Province")

    
    create=st.button("Create")


    if col1 and col2 and col3 and col4 and col5 and col6 and create:
        dbb.emp_insert(q, w, e, r, t, y, u, i, o)
        data=dbb.update_emp(q)
        df = pd.DataFrame([data], columns=['ID','Phone Number','First Name','Middle Name',"Last Name",'Street Number','Street Name','City','Province'])
        st.write(df)
        st.success("Data is inserted successfully")

        

if selected == "Update Employee Details":
    try:
        a = st.text_input("ID")
        bu = st.button("Find")
        
        if  dbb.update_emp(a) is not None:
            data=dbb.update_emp(a)
            df = pd.DataFrame([data], columns=['ID','Phone Number','First Name','Middle Name',"Last Name",'Street Number','Street Name','City','Province'])
            st.write(df)
            col2,col3,col4,col5 =  st.columns([2,2,2,2])
            col6,col7,col8,col9,col10=st.columns([2,5,2,2,2])
            with col2:
                w=st.text_input("Phone Number",value=data[1])
            with col3:
                e=st.text_input("First Name",value=data[2])
            with col4:
                r=st.text_input("Middle Name",value=data[3])
            with col5:
                t=st.text_input("Last Name",value=data[4])
            with col6:
                y=st.text_input("Street Number",value=data[5])
            with col7:
                u=st.text_input("Street Name",value=data[6])
            with col8:
                i=st.text_input("City",value=data[7])
            with col9:
                o=st.text_input("Province",value=data[8])
            update=st.button("update")

            if  col2 and col3 and col4 and col5 and col6 and update:
                st.markdown("Here is previous data")
                st.write(df)
                query = """UPDATE Employees 
                SET phone_number = ?, first_name = ?, middle_name = ?, last_name = ?, 
                    street_number = ?, street_name = ?, city = ?, province = ?
                WHERE employee_id = ?"""
                data = (w, e, r, t, y, u, i, o, a)
                
                connection = sqlite3.connect("warehouse.db")
                cursor = connection.cursor()
                cursor.execute(query, data)
                connection.commit()
                st.write("Updated data is")
                data=dbb.update_emp(a)
                df = pd.DataFrame([data], columns=['ID','Phone Number','First Name','Middle Name',"Last Name",'Street Number','Street Name','City','Province'])
                st.write(df)
                
        else :
            st.error("No Data Found")
    except :
        st.write("Enter valid Id")


if selected =="Delete Employee Record":
    a=st.text_input("Enter Id")
    dele=st.button("Delete")
    if dele and dbb.update_emp(a) is not None :
        data=dbb.update_emp(a)
        df = pd.DataFrame([data], columns=['ID','Phone Number','First Name','Middle Name',"Last Name",'Street Number','Street Name','City','Province'])
        st.write("The following data is deleted")
        st.write(df)
        dbb.emp_del(a)
        st.success("Data has been deleted")
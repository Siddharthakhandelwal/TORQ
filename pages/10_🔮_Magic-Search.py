import database_ware as dbb
import streamlit as st
import os
import sqlite3
import database_ware as dbb
import matplotlib.pyplot as plt
from helperSqllte import *
from helper import *
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
## Configure Genai Key

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(
    page_title='Magic-Search', 
    layout='wide',
    page_icon="🔮"               
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

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Function To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name `warehouse.db` database with the following structure:

    Table: Warehouses
    Columns:
    - warehouse_id (INT) [Primary Key, Auto Increment]
    - warehouse_symbol (CHAR(4)) [Unique, Not Null]

    Table: Bins
    Columns:
    - bin_number (INT) [Primary Key]
    - warehouse_id (INT) [Not Null]
    - capacity (INT) [Not Null]
    Foreign Key:
    - References Warehouses(warehouse_id)

    Table: Parts
    Columns:
    - part_number (VARCHAR(5)) [Primary Key]
    - assembly_id (INT)
    Foreign Key:
    - References Assemblies(assembly_id)

    Table: Assemblies
    Columns:
    - assembly_id (INT) [Primary Key, Auto Increment]

    Table: Batches
    Columns:
    - batch_number (INT) [Primary Key, Auto Increment]
    - part_number (VARCHAR(5)) [Not Null]
    - date_in (DATE) [Not Null]
    - size (INT) [Not Null]
    - bin_number (INT) [Not Null]
    - manager_id (INT) [Not Null]
    Foreign Keys:
    - References Parts(part_number)
    - References Bins(bin_number)
    - References Employees(employee_id)

    Table: Backorders
    Columns:
    - backorder_id (INT) [Primary Key, Auto Increment]
    - part_number (VARCHAR(5)) [Not Null]
    - manager_id (INT) [Not Null]
    - date_backordered (DATE) [Not Null]
    - quantity_backordered (INT) [Not Null]
    - remaining_quantity (INT) [Not Null]
    Foreign Keys:
    - References Parts(part_number)
    - References Employees(employee_id)

    Table: Shipments
    Columns:
    - shipment_id (INT) [Primary Key, Auto Increment]
    - batch_number (INT) [Not Null]
    - date_out (DATE) [Not Null]
    - employee_id (INT) [Not Null]
    Foreign Keys:
    - References Batches(batch_number)
    - References Employees(employee_id)

    Table: Employees
    Columns:
    - employee_id (INT) [Primary Key, Auto Increment]
    - phone_number (INT) [Unique, Not Null]
    - first_name (VARCHAR(10)) [Not Null]
    - middle_name (VARCHAR(10)]
    - last_name (VARCHAR(20)) [Not Null]
    - street_number (VARCHAR(6)) [Not Null]
    - street_name (VARCHAR(20)) [Not Null]
    - city (VARCHAR(20)) [Not Null]
    - province (CHAR(2)) [Not Null]

    Table: Managers
    Columns:
    - manager_id (INT) [Primary Key]
    Foreign Key:
    - References Employees(employee_id)
    \n\nFor example,\nExample 1 - Tell me the total number of employees?, 
        the SQL command will be something like this SELECT COUNT(*) FROM Employees ;
        \nExample 2 - Tell me all the employees who are managers?, 
        the SQL command will be something like this SELECT * FROM Employees
        WHERE employee_id IN (SELECT manager_id FROM Managers); 
        \nExample 3 - Give all employee numbers for all the workers that work under a manager with the first name "Tony7" 
        and the last name "Tona7" with no middle name?, the SQl command will be something like this SELECT employee_id
        FROM Employees WHERE employee_id IN (SELECT manager_id FROM Managers WHERE manager_id IN (
        SELECT employee_id FROM Employees WHERE first_name = 'Tony7' AND last_name = 'Tona7' AND middle_name IS NULL));
        \nExample 4 - Give all the names and employee numbers for all the workers, listed in alphabetical order 
        (by last name, then by first name, then by middle name), the SQL command will be something like this 
        SELECT employee_id, first_name || ' ' || last_name AS full_name FROM Employees
        ORDER BY last_name, first_name, middle_name;
        \nExample 5 - Give all the phone numbers and employee numbers for all the managers, the SQL command will be something like
        this SELECT e.employee_id, e.phone_number FROM Employees e JOIN Managers m ON e.employee_id = m.manager_id;
        \nExample 7 - For each manager, list all current and old backorders done by the manager. For  each backorder you have to list the part_no, backorder date, 
        and fulfilled date.  For current backorders, list a phony fulfilled date '2000-01-01', the SQL command will be something
        like this SELECT e.employee_id AS manager_id,bo.part_number,bo.date_backordered AS backorder_date,IFNULL(s.date_out, '2000-01-01') AS fulfilled_date
        FROM Backorders bo JOIN Parts p ON bo.part_number = p.part_number LEFT JOIN Shipments s ON bo.backorder_id = s.batch_number
        JOIN Employees e ON bo.manager_id = e.employee_id;

        also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App

# st.header("Gemini App To Retrieve SQL Data")

st.markdown(
        """
                <div style="text-align: center;">
                    <h1>Magic-Search 🔮🤖🛠️🕹️</h1>
                    <h3>I can generate SQL queries as well !!!</h3>
                    <h4>With Explanation as well !!!</h4>
                    <p>This tool is a simple tool that allows you to generate SQL queries based on your prompts</p>
                
                </div>

        """,
        unsafe_allow_html=True,
    )


question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

connection=sqlite3.connect("warehouse.db")
cursor=connection.cursor()

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    st.success("SQL Query Generated Successfully! Here is your Query Below:")
    st.code(response,language="sql")
    st.subheader("The Response is")
    df = sqltopd(response,connection)

    # Retrieve column names from cursor description if available
    cursor = connection.cursor()
    column_names = None
    if cursor.description:
        column_names = [col[0] for col in cursor.description]

    # Insert column names as the first row of the DataFrame if available
    if column_names:
        df.columns = column_names
        
    st.write(df)
    

    # df = sqltopd(response,connection)
    # st.write(df)
    # for row in response:
    #     print(row)
    #     st.header(row)

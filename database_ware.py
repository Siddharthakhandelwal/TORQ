import sqlite3
import pandas as pd
import streamlit as st

# Connect to the database
connection = sqlite3.connect("warehouse.db")


# Table creation functions (remove if tables already exist)
def create_assem():
    connection = sqlite3.connect("warehouse.db")
    """Creates the Assemblies table."""
    connection.execute('''CREATE TABLE IF NOT EXISTS Assemblies (
        assembly_id INT PRIMARY KEY )''')

def backorders_create():
    
    connection = sqlite3.connect("warehouse.db")
    """Creates the Backorders table."""
    connection.execute('''CREATE TABLE IF NOT EXISTS Backorders (
        backorder_id INT PRIMARY KEY,
        part_number VARCHAR(5) NOT NULL,
        manager_id INT NOT NULL,
        date_backordered DATE NOT NULL,
        quantity_backordered INT NOT NULL,
        remaining_quantity INT NOT NULL,
        FOREIGN KEY (part_number) REFERENCES Parts(part_number),
        FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
    )''')

def batches_create():
    """Creates the Batches table."""
    connection = sqlite3.connect("warehouse.db")
    connection.execute('''CREATE TABLE IF NOT EXISTS Batches (
        batch_number INT PRIMARY KEY,
        part_number VARCHAR(5) NOT NULL,
        date_in DATE NOT NULL,
        size INT NOT NULL,
        bin_number INT NOT NULL,
        manager_id INT NOT NULL,
        FOREIGN KEY (part_number) REFERENCES Parts(part_number),
        FOREIGN KEY (bin_number) REFERENCES Bins(bin_number),
        FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
    )''')

def bins_create():
    connection = sqlite3.connect("warehouse.db")
    """Creates the Bins table."""
    connection.execute('''CREATE TABLE IF NOT EXISTS Bins (
        bin_number INT PRIMARY KEY,
        warehouse_id INT NOT NULL,
        capacity INT NOT NULL,
        FOREIGN KEY (warehouse_id) REFERENCES Warehouses(warehouse_id)
    )''')

def emp_create():
    connection = sqlite3.connect("warehouse.db")
    """Creates the Employees table."""
    connection.execute('''CREATE TABLE IF NOT EXISTS Employees (
        employee_id INT PRIMARY KEY,
        phone_number INT  NOT NULL,
        first_name VARCHAR(10) NOT NULL,
        middle_name VARCHAR(10),
        last_name VARCHAR(20) NOT NULL,
        street_number VARCHAR(6) NOT NULL,
        street_name VARCHAR(20) NOT NULL,
        city VARCHAR(20) NOT NULL,
        province CHAR(2) NOT NULL
    )''')

def mana_create():
    connection = sqlite3.connect("warehouse.db")
    """Creates the Managers table."""
    connection.execute('''CREATE TABLE IF NOT EXISTS Managers (
        manager_id INT PRIMARY KEY,
        FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
    )''')

def parts_create():
    connection = sqlite3.connect("warehouse.db")
    """Creates the Parts table."""
    connection.execute('''CREATE TABLE IF NOT EXISTS Parts (
        part_number VARCHAR(5) PRIMARY KEY,
        assembly_id INT,
        FOREIGN KEY (assembly_id) REFERENCES Assemblies(assembly_id)
    )''')

def shipmemts_create():
    connection = sqlite3.connect("warehouse.db")
    """Creates the Shipments table."""
    connection.execute('''CREATE TABLE IF NOT EXISTS Shipments (
        shipment_id INT PRIMARY KEY,
        batch_number INT NOT NULL,
        date_out DATE NOT NULL,
        employee_id INT NOT NULL,
        FOREIGN KEY (batch_number) REFERENCES Batches(batch_number),
        FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
    )''')

def warehouse_create():
    connection = sqlite3.connect("warehouse.db")
    """Creates the Warehouses table."""
    connection.execute('''CREATE TABLE IF NOT EXISTS Warehouses (
        warehouse_id INT PRIMARY KEY,
        warehouse_symbol CHAR(4) UNIQUE NOT NULL
    )''')


# Data insertion functions using parameterized queries for better security
def war_insert(q, w):
    connection = sqlite3.connect("warehouse.db")
    """Inserts data into the Warehouses table."""
    querry = '''INSERT INTO Warehouses (warehouse_id, warehouse_symbol) VALUES (?, ?)'''
    data = (q, w)
    connection.execute(querry, data)
    connection.commit()

def bin_insert(q, w, r):
    connection = sqlite3.connect("warehouse.db")
    """Inserts data into the Bins table."""
    querry = '''INSERT INTO Bins (bin_number, warehouse_id, capacity) VALUES (?, ?, ?)'''
    data = (q, w, r)
    connection.execute(querry, data)
    connection.commit()

def part_insert(q,w):
        connection = sqlite3.connect("warehouse.db")
        querry='''INSERT INTO Parts (part_number,assembly_id) VALUES (?,?)'''
        data=(q,w)
        connection.execute(querry,data)
        connection.commit()

def batch_insert(a,b,w,e,r,t):
        connection = sqlite3.connect("warehouse.db")
        querry='''INSERT INTO Batches (batch_number,part_number, date_in, size, bin_number, manager_id) VALUES (?,?,?,?,?,?)'''
        data=(a,b,w,e,r,t)
        connection.execute(querry,data)
        connection.commit()

def emp_insert(q,w,e,r,t,y,u,i,o):
        connection = sqlite3.connect("warehouse.db")
        querry='''INSERT INTO Employees (employee_id,phone_number, first_name,middle_name, last_name, street_number, street_name, city, province) VALUES (?,?,?,?,?,?,?,?,?)'''
        data=(q,w,e,r,t,y,u,i,o)
        connection.execute(querry,data)
        connection.commit()
        

def mana_insert(a):
        connection = sqlite3.connect("warehouse.db")
        querry='''INSERT INTO Managers (manager_id) VALUES (?)'''
        data=(a,)
        connection.execute(querry,data)
        connection.commit()


def ass_insert(q):
        connection = sqlite3.connect("warehouse.db")
        querry=f"INSERT INTO Assemblies (assembly_id) VALUES ({q})"
        
        connection.execute(querry)
        connection.commit()


def back_insert(a,b,c,d,e,f):
        querry='''INSERT INTO Backorders ( backorder_id,part_number, manager_id, date_backordered, quantity_backordered, remaining_quantity) VALUES (?,?,?,?,?,?)'''
        data=(a,b,c,d,e,f)
        connection = sqlite3.connect("warehouse.db")
        connection.execute(querry,data)
        connection.commit()

def ship_insert(q,w,e,r):
        querry='''INSERT INTO Shipments ( shipment_id,batch_number, date_out, employee_id) VALUES (?,?,?,?)'''
        data=(q,w,e,r)
        connection = sqlite3.connect("warehouse.db")
        connection.execute(querry,data)
        connection.commit()

def ware_del(q):
        querry="DELETE FROM Warehouses WHERE warehouse_id = ?"
        data=(q,)
        connection = sqlite3.connect("warehouse.db")
        if connection.execute(querry,data):
             connection.commit()
             return True
        else:
             return False
def bin_del(q):
        querry="DELETE FROM Bins WHERE bin_number = ?"
        data=(q,)
        connection = sqlite3.connect("warehouse.db")
        if connection.execute(querry,data):
             connection.commit()
             return True
        else:
             return False
def parts_del(q):
        querry="DELETE FROM Parts WHERE part_number = ?"
        data=(q,)
        connection = sqlite3.connect("warehouse.db")
        if connection.execute(querry,data):
             connection.commit()
             return True
        else:
             return False

def ass_del(q):
        querry=f"DELETE FROM Assemblies WHERE assembly_id = {q}"        
        connection = sqlite3.connect("warehouse.db")
        if connection.execute(querry):
             connection.commit()
             return True
        else:
             return False

def batches_del(q):
        querry="DELETE FROM Batches WHERE batch_number = ?"
        data=(q,)
        connection = sqlite3.connect("warehouse.db")
        if connection.execute(querry,data):
             connection.commit()
             return True
        else:
             return False

def back_del(q):
        querry="DELETE FROM Backorders WHERE backorder_id = ?"
        data=(q,)
        connection = sqlite3.connect("warehouse.db")
        if connection.execute(querry,data):
             connection.commit()
             return True
        else:
             return False
def ship_del(q):
        querry="DELETE FROM Shipments WHERE shipment_id = ?"
        data=(q,)
        connection = sqlite3.connect("warehouse.db")
        if connection.execute(querry,data):
             connection.commit()
             return True
        else:
             return False
def emp_del(q):
        querry="DELETE FROM Employees WHERE employee_id = ?"
        data=(q,)
        connection = sqlite3.connect("warehouse.db")
        if connection.execute(querry,data):
             connection.commit()
             return True
        else:
             return False
def man_del(q):
        querry="DELETE FROM Managers WHERE manager_id = ?"
        data=(q,)
        connection = sqlite3.connect("warehouse.db")
        if connection.execute(querry,data):
             connection.commit()
             return True
        else:
             return False

def update_emp(q):
    query = f"SELECT employee_id, phone_number, first_name, middle_name, last_name, street_number, street_name, city, province FROM Employees WHERE employee_id = {q}"
    connection = sqlite3.connect("warehouse.db")
    result = connection.execute(query)
    emp = result.fetchone()  
    
    if emp is not None:
        return emp
def update_manager(q):
    query = f"SELECT manager_id FROM Managers WHERE manager_id = {q}"
    connection = sqlite3.connect("warehouse.db")
    result = connection.execute(query)
    manager = result.fetchone()  
    
    if manager is not None:
        df = pd.DataFrame([manager], columns=['Manager ID'])
        return df

def update_assembly(q):
    query = f"SELECT assembly_id FROM Assemblies WHERE assembly_id = {q}"
    connection = sqlite3.connect("warehouse.db")
    result = connection.execute(query)
    assembly = result.fetchone()  # Fetch only one row
    
    if assembly is not None:
        df = pd.DataFrame([assembly], columns=['Assembly ID'])
        return df

def update_bin(q):
    query = f"SELECT bin_number, warehouse_id, capacity FROM Bins WHERE bin_number = {q}"
    connection = sqlite3.connect("warehouse.db")
    result = connection.execute(query)
    bin_data = result.fetchone()  # Fetch only one row
    
    if bin_data is not None:
        df = pd.DataFrame([bin_data], columns=['Bin Number', 'Warehouse ID', 'Capacity'])
        return bin_data
def update_part(q):
    query = f"SELECT part_number, assembly_id FROM Parts WHERE part_number = '{q}'"
    connection = sqlite3.connect("warehouse.db")
    result = connection.execute(query)
    part_data = result.fetchone()  # Fetch only one row
    
    if part_data is not None:
        df = pd.DataFrame([part_data], columns=['Part Number', 'Assembly ID'])
        return part_data
def update_shipment(q):
    query = f"SELECT shipment_id, batch_number, date_out, employee_id FROM Shipments WHERE shipment_id = {q}"
    connection = sqlite3.connect("warehouse.db")
    result = connection.execute(query)
    shipment_data = result.fetchone()  # Fetch only one row
    
    if shipment_data is not None:
        df = pd.DataFrame([shipment_data], columns=['Shipment ID', 'Batch Number', 'Date Out', 'Employee ID'])
        return shipment_data
def update_backorder(q):
    query = f"SELECT backorder_id, part_number, manager_id, date_backordered, quantity_backordered, remaining_quantity FROM Backorders WHERE backorder_id = {q}"
    connection = sqlite3.connect("warehouse.db")
    result = connection.execute(query)
    backorder_data = result.fetchone()  # Fetch only one row
    
    if backorder_data is not None:
        df = pd.DataFrame([backorder_data], columns=['Backorder ID', 'Part Number', 'Manager ID', 'Date Backordered', 'Quantity Backordered', 'Remaining Quantity'])
        return backorder_data
def update_warehouse(q):
    query = f"SELECT warehouse_id, warehouse_symbol FROM Warehouses WHERE warehouse_id = {q}"
    connection = sqlite3.connect("warehouse.db")
    result = connection.execute(query)
    warehouse_data = result.fetchone()  # Fetch only one row
    
    if warehouse_data is not None:
        
        return warehouse_data
def update_batch(q):
    query = f"SELECT batch_number, part_number, date_in, size, bin_number, manager_id FROM Batches WHERE batch_number = {q}"
    connection = sqlite3.connect("warehouse.db")
    result = connection.execute(query)
    batch_data = result.fetchone()  # Fetch only one row
    
    if batch_data is not None:
        df = pd.DataFrame([batch_data], columns=['Batch Number', 'Part Number', 'Date In', 'Size', 'Bin Number', 'Manager ID'])
        return batch_data

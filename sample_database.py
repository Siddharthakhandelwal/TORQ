# import sqlite3


# # Connect to the database
# connection = sqlite3.connect("warehouse.db")

# cur=connection.cursor()

# cur.execute("""
# INSERT INTO Batches (batch_number, part_number, date_in, size, bin_number, manager_id)
# VALUES
# (1, 'P001', '2024-04-01', 50, 101, 1),
# (2, 'P002', '2024-04-02', 100, 102, 1),
# (3, 'P003', '2024-04-03', 75, 201, 2),
# (4, 'P004', '2024-04-04', 120, 301, 2),
# (5, 'P005', '2024-04-05', 150, 302, 3),
# (6, 'P006', '2024-04-06', 200, 401, 3),
# (7, 'P007', '2024-04-07', 180, 402, 4);

#                 """)
# connection.commit()

# ## no use of this file...used this just to populate the database
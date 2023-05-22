# Task 1. Create a SQLite database. Using SQL queries, create a table
# in the created database that should contain the following fields:
# - id - the value for each new element should by default be +1 from the previous one
# - first_name is a text value
# - last_name is a text value
# - age is a number
#
# Task 2. Create SQL queries to add records to the created table.
# Create requests to add a minimum of 5 different records.

import sqlite3

db_name = "users"
data = [
    ('Vitalii', 'Grebennikov', 35),
    ('Oleksii', '', 32),
    ('Oleksandr', '', 30),
    ('Klavdia', '', 32),
    ('Serhiy', 'Moskalenko', 40)
]

# create a connection
db = sqlite3.connect("db.sqlite")

cur = db.cursor()

# create a table
cur.execute(f"CREATE TABLE IF NOT EXISTS {db_name}"
            "(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
            "first_name TEXT, "
            "last_name TEXT, "
            "age INTEGER NOT NULL)")
print(f'Table "{db_name}" created successfully')

# insert a data
cur.executemany(f"INSERT INTO {db_name} (first_name, last_name, age) VALUES (?, ?, ?)", data)
db.commit()
print('New records inserted successfully')

# select a data
res = cur.execute(f"SELECT * FROM {db_name}")
print(res.fetchall())

# close a connection
db.close()

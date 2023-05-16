# Task 3. (optional) For the table creation request from task 1,
# change first_name and last_name so that it is not possible to add
# an empty value.
#
# Task 4. (optional) For the request to create a table from task 1,
# change first_name and last_name so that it is not possible to add
# an already existing combination of first_name and last_name.

import sqlite3

db_name = "new_users"
data = [
    ('Vitalii', 'Grebennikov', 35),
    ('John', 'Snow', 32),
    ('Oleksandr', 'Makedonskii', 30),
    ('Claudia', 'Schiffer', 32),
    ('Serhiy', 'Moskalenko', 40)
]

try:
    # create a connection
    db = sqlite3.connect("db.sqlite")

    with db:
        cur = db.cursor()

        # create a table
        cur.execute(f"CREATE TABLE IF NOT EXISTS {db_name}"
                    "(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
                    "first_name TEXT NOT NULL UNIQUE, "
                    "last_name TEXT NOT NULL UNIQUE, "
                    "age INTEGER NOT NULL, "
                    "CONSTRAINT check_first_name CHECK (first_name <> ''), "
                    "CONSTRAINT check_last_name CHECK (last_name <> ''), "
                    "CONSTRAINT check_age CHECK (age > 0))")
        print(f'Table "{db_name}" created successfully')

        # insert a data
        cur.executemany(f"INSERT INTO {db_name} (first_name, last_name, age) VALUES (?, ?, ?)", data)
        db.commit()
        print('New records inserted successfully')

        # select a data
        res = cur.execute(f"SELECT * FROM {db_name}")
        print(res.fetchall())

        # trying insert new item with empty data
        cur.execute(f"INSERT INTO {db_name} (first_name, last_name, age) VALUES ('', '', 0)")
        db.commit()
        print('New empty record inserted successfully')  # It will never be handled

except sqlite3.IntegrityError as err:
    print(str(err))
except sqlite3.Error as error:
    print(str(error))

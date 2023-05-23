# Using the database from additional lecture materials:
# Task 1. Write a SQL query that will select all entries from
# the users table older than 30 years.
#
# Task 2. Write a sql query that will display the number of entries
# in the users table that are older than 30 years.
#
# Task 3. Write a sql query that will display information about the age
# (number of years) and the number of users who correspond to this age.
# The result of executing such a request should be a table:
#      age | users
#      32 | 1
#      52 | 2
#      120 | 2
#      1142 | 1
#
# Task 4. Write an sql query that will do the same as in task 3, but output
# the data sorted by the number of users in descending order and by age
# in ascending order. The result should be a table:
#      age | users
#      52 | 2
#      120 | 2
#      32 | 1
#      1142 | 1
#
# Task 5. (optional) Modify the previous query in such a way as to select
# from the obtained result only those records where the value of users is
# greater than 1. The result should be a table:
#      age | users
#      52 | 2
#      120 | 2


import sqlite3
from sqlite3 import Error
from pprint import pprint

db = "database_1.sqlite"
table_name = "users"


def divider():
    print('=' * 30)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def users_older_then(cur, age):
    # Task 1
    res = cur.execute(f"SELECT * FROM {table_name} WHERE age > {age}")
    return res.fetchall()


def count_users_older_then(cur, age):
    # Task 2
    res = cur.execute(f"SELECT COUNT(id) FROM {table_name} WHERE age > {age}")
    return res.fetchone()[0]


def tbl_num_of_users_with_age(cur):
    # Task 3
    res = cur.execute(f"SELECT age, COUNT(id) AS users "
                      f"FROM {table_name} "
                      f"GROUP BY age")
    return res.fetchall()


def sorted_tbl_num_of_users_with_age(cur, sort_params, having_params=None):
    # Task 4
    sort_criteria = []
    sort_query = ""

    for column, direction in sort_params.items():
        sort_criteria.append(f"{column} {direction.upper()}")

    if sort_criteria:
        sort_query = "ORDER BY " + ", ".join(sort_criteria)

    # Task 5
    having_query = ""
    if having_params:
        having_query = f"HAVING {having_params}"

    res = cur.execute(f"SELECT age, COUNT(id) AS users "
                      f"FROM {table_name} "
                      f"GROUP BY age "
                      f"{having_query} "
                      f"{sort_query}")
    return res.fetchall()


def print_table(cols, rows):
    print(' | '.join(cols))
    print('-' * 24)

    for row in rows:
        print(' | '.join(map(str, row)))


def main():
    conn = create_connection(db)

    with conn:
        cur = conn.cursor()
        age = 30

        print(f"Task 1: List of users older than {age} years:")
        pprint(users_older_then(cur, age))
        divider()

        print(f"Task 2: Number of users over {age} years old: {count_users_older_then(cur, age)}")
        divider()

        print("Task 3: The age and the number of users who correspond to this age:")
        rows = tbl_num_of_users_with_age(cur)
        print_table(['age', 'users'], rows)
        divider()

        print("Task 4: The age and the number of users who correspond to this age\n"
              "(the data sorted by the number of users in descending order and by age in ascending order):")
        rows = sorted_tbl_num_of_users_with_age(cur, {'users': 'desc', 'age': 'asc'})
        print_table(['age (ASC)', 'users (DESC)'], rows)
        divider()

        print("Task 5: The age and the number of users who correspond to this age\n"
              "(the data sorted by the number of users in descending order and by age in ascending order).\n"
              "Selected only those records where the value of users is greater than 1:")
        rows = sorted_tbl_num_of_users_with_age(cur, {'users': 'desc', 'age': 'asc'}, 'users > 1')
        print_table(['age (ASC)', 'users (DESC)'], rows)
        divider()


if __name__ == '__main__':
    main()

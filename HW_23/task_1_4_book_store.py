# Let's imagine that we work with an online store that sells books.
# To check requests, you can use the database at the link.
#
# Task 1: To record information about users, books, publishers and sales,
# create the following tables:
# - users: id, first_name, last_name, age
# - publishing_house: id, name, rating (default 5)
# - books: id, title, author, year, price, publishing_house_id
# - purchases: id, user_id, book_id, date
# With:
# - publishing_house_id is the FOREIGN KEY of the publishing_houses table
# - user_id is the FOREIGN KEY of the users table
# - book_id is the FOREIGN KEY of the books table
#
# Task 2: Write a query that will display the date of the purchase and
# the name of the user who made it.
# The result should be in the format:
#   purchases.id, purchases.date, user.first_name, user.last_name
#
# Task 3: Write a query that will display all users and the names of all
# the books they bought, sort the data by user_id.
# The result should be presented in the format:
#   users.id, users.first_name, users.last_name, books.title
#
# Task 4 (optional): Write the following requests:
# - a query that will calculate the sum of all purchases for each user.
# The result should be in the format:
#   users.id, users.first_name, users.last_name, total_purchases
# - a query that will display the number of book purchases for each user.
# The result should be presented in the format:
#   user.id, purchases_count
# - a query that returns the number of book purchases for author Rowling.
# The result should be presented in the format: amount
# - a query that will display the sales totals for each author and
# the number of purchases.
# - a query that will display all book titles with their number of
# sales in descending order of number of sales.


import sqlite3
from sqlite3 import Error
from pprint import pprint

db = "book_store.sqlite"


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


def divider():
    print('=' * 30)


def create_tbl_users(cur):
    # Task 1: Create table 'users'
    cur.execute("CREATE TABLE IF NOT EXISTS 'users'"
                "(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
                "first_name TEXT NOT NULL UNIQUE CHECK (first_name <> ''), "
                "last_name TEXT NOT NULL UNIQUE CHECK (last_name <> ''), "
                "age INTEGER NOT NULL CHECK (age > 0))")


def create_tbl_publishing_houses(cur):
    # Task 1: Create table 'publishing_houses'
    cur.execute("CREATE TABLE IF NOT EXISTS 'publishing_houses'"
                "(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
                "name TEXT NOT NULL CHECK (name <> ''), "
                "rating INTEGER DEFAULT 5)")


def create_tbl_books(cur):
    # Task 1: Create table 'books'
    cur.execute("CREATE TABLE IF NOT EXISTS 'books'"
                "(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
                "title TEXT NOT NULL CHECK (title <> ''), "
                "author TEXT NOT NULL CHECK (author <> ''), "
                "year INTEGER NOT NULL, "
                "price INTEGER NOT NULL, "
                "publishing_house_id INTEGER NOT NULL, "
                "FOREIGN KEY (publishing_house_id) references publishing_houses(id))")


def create_tbl_purchases(cur):
    # Task 1: Create table 'purchases'
    cur.execute("CREATE TABLE IF NOT EXISTS 'purchases'"
                "(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
                "user_id INTEGER NOT NULL, "
                "book_id INTEGER NOT NULL, "
                "date TEXT DEFAULT CURRENT_TIMESTAMP, "
                "FOREIGN KEY (user_id) references users(id), "
                "FOREIGN KEY (book_id) references books(id))")


def select_purchases_date(cur):
    # Task 2: Select the date of the purchase and the name of the user who made it
    res = cur.execute("SELECT purchases.id, purchases.date, users.first_name, users.last_name "
                      "FROM purchases "
                      "LEFT JOIN users ON users.id = purchases.user_id")
    return res.fetchall()


def select_user_books(cur):
    # Task 3: Select all users and the names of all the books they bought, sort the data by user_id
    res = cur.execute("SELECT users.id, users.first_name, users.last_name, books.title "
                      "FROM users "
                      "LEFT JOIN purchases ON users.id = purchases.user_id "
                      "LEFT JOIN books ON books.id = purchases.book_id "
                      "ORDER BY users.id")
    return res.fetchall()


def select_user_purchases_summ(cur):
    # Task 4.1: Calculate the sum of all purchases for each user.
    res = cur.execute("SELECT users.id, users.first_name, users.last_name, SUM(books.price) AS total_purchases "
                      "FROM users "
                      "LEFT JOIN purchases ON users.id = purchases.user_id "
                      "LEFT JOIN books ON books.id = purchases.book_id "
                      "GROUP BY users.id")
    return res.fetchall()


def select_user_book_purchases_num(cur):
    # Task 4.2: Display the number of book purchases for each user.
    res = cur.execute("SELECT users.id, COUNT(purchases.id) AS purchases_count "
                      "FROM users "
                      "LEFT JOIN purchases ON users.id = purchases.user_id "
                      "GROUP BY users.id")
    return res.fetchall()


def select_rowlings_books_purchases_num(cur):
    # Task 4.3: Display the number of book purchases for each user.
    res = cur.execute("SELECT SUM(books.price), COUNT(purchases.id) AS purchases_count "
                      "FROM purchases "
                      "LEFT JOIN books ON books.id = purchases.book_id "
                      "WHERE books.author = 'Rowling' "
                      "GROUP BY books.author")
    return res.fetchall()


def select_author_books_purchases_num(cur):
    # Task 4.4: Display the sales totals for each author and the number of purchases.
    res = cur.execute("SELECT books.author, SUM(books.price), COUNT(purchases.id) AS purchases_count "
                      "FROM purchases "
                      "LEFT JOIN books ON books.id = purchases.book_id "
                      "GROUP BY books.author")
    return res.fetchall()


def select_books_purchases_num(cur):
    # Task 4.5: Display all book titles with their number of sales in descending order of number of sales.
    res = cur.execute("SELECT books.title, COUNT(purchases.id) AS purchases_count "
                      "FROM purchases "
                      "LEFT JOIN books ON books.id = purchases.book_id "
                      "GROUP BY books.title "
                      "ORDER BY purchases_count DESC")
    return res.fetchall()


def print_res(rows):
    pprint(rows)
    divider()


def main():
    conn = create_connection(db)

    with conn:
        cur = conn.cursor()

        print("Task 1: Create db tables")

        print("Create table 'users'")
        create_tbl_users(cur)

        print("Create table 'publishing_houses'")
        create_tbl_publishing_houses(cur)

        print("Create table 'books'")
        create_tbl_books(cur)

        print("Create table 'purchases'")
        create_tbl_purchases(cur)
        divider()

        print("Task 2: Display the date of the purchase and the name of the user who made it")
        print_res(select_purchases_date(cur))

        print("Task 3: Display all users and the names of all the books they bought, sort the data by user_id")
        print_res(select_user_books(cur))

        print("Task 4.1: Display calculation the sum of all purchases for each user")
        print_res(select_user_purchases_summ(cur))

        print("Task 4.2: Display the number of book purchases for each user")
        print_res(select_user_book_purchases_num(cur))

        print("Task 4.3: Display the number of book purchases for author Rowling")
        print_res(select_rowlings_books_purchases_num(cur))

        print("Task 4.4: Display the sales totals for each author and the number of purchases")
        print_res(select_author_books_purchases_num(cur))

        print("Task 4.5: Display all book titles with their number of sales in descending order of number of sales")
        print_res(select_books_purchases_num(cur))


if __name__ == '__main__':
    main()


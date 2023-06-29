# 1. Create functions to process such requests:
# - GET /users – should return a random list of names (any number)
# - GET /books – should return a random list of books (any number) in the form of an html list
#
# 2. Create request handler functions for GET /users and GET /books
# that should accept url parameters (/users/1, /books/kobzar):
# - For /users – id, which can only be a numeric value. If the value of
# id is divisible by 2 - return the text with this value. If not shared
# - return status 404 Not Found
# - For /books – title, text value. Transform the first letter of title
# into uppercase, and all others into lowercase (using one of the str methods),
# return the transformed value as a response
#
# 3. Create a function for processing GET /params requests - it should return
# an HTML table that will contain the keys and values of the query parameters.
# For example, when requesting GET /params?name=Test&age=1, the page should display:
# parameter | value
# name | Test
# age | 1
#
# 4. Create a function for processing GET, POST /login requests - at a GET request,
# it should return an HTML form (method=POST, action=/login), which should contain
# the fields username, password and the submit button.
# When making a POST request, it should check whether the username and password
# are included in the request data:
# - If the request contains this data, you need to redirect the user to the /users page.
# - If not, a 400 error should be returned with information about missing data.
#
# 5. (optional) Create custom 404 and 500 error handlers that should return custom html code for display.
#
# 6. (optional) Create a GET / request handler that should return html code
# with links to the pages /login, /users, /books, /params
#
# 7. (optional) Modify the /users and /books handler functions from the first
# task so that they return the exact number of values based on the query param
# count: /users?count=20 should return 20 values. If the parameter is not passed,
# the number must be random.
#
# 8. (optional) Add username and password validation to the POST /login handler function:
# - Username at least 5 characters
# - Password must contain at least 1 number and 1 capital letter, must be at least 8 characters

import random
import string
import re
from flask import abort, request, redirect
from app import app

first_names = ["Vitalii", "Serhii", "Oleksandr", "Dmytro", "Oksana", "Nadiia", "Sofiia",
               "Stepan", "Petro", "Bogdan", "Vasyl", "Ivan", "Maksym", "Artem"]
last_names = ["Hrebennikov", "Serhiienko", "Dmytrenko", "Mostovenko", "Petrenko", "Oleksienko", "Kovalenko",
              "Stepanenko", "Vasylenko", "Bovtruk", "Bondarenko", "Ivanenko", "Maksymenko", "Moskalenko"]


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_titles(length):
    titles = []
    for _ in range(length):
        titles.append(generate_random_string(random.randint(5, 25)).capitalize())

    return titles


# Tasks 1, 7
@app.route('/users')
def get_users():
    filters = request.values
    try:
        cnt = int(filters.get('count')) if filters.get('count') else random.randint(1, 100)
    except ValueError:
        abort(400, 'Invalid count value')

    # ===== generate users
    users = []
    for _ in range(cnt):
        users.append(random.choice(first_names) + ' ' + random.choice(last_names))

    return users, 200


# Tasks 1, 7
@app.get('/books')
def get_books():
    filters = request.values
    try:
        cnt = int(filters.get('count')) if filters.get('count') else random.randint(1, 100)
    except ValueError:
        abort(400, 'Invalid count value')

    titles = generate_random_titles(cnt)

    books = ''.join([
        f"<li>{title}</li>"
        for title in titles
    ])

    response = f'''
    <h1>Book List</h1>
    <ul>
        {books}
    </ul>
    '''
    return response, 200


# Task 2
@app.get('/users/<user_id>')
def get_user(user_id):
    try:
        user_id_int = int(user_id)
    except ValueError:
        abort(400, 'Invalid user id')

    if user_id_int % 2 == 0:
        return f'User ID: {user_id_int}', 200

    abort(404, 'User not found')


# Tasks 2
@app.get('/books/<name>')
def get_book(name):
    if name.isnumeric():
        abort(400, 'Invalid book name')
    return name.capitalize(), 200


# Task 3
@app.get('/params')
def get_params():
    params = request.values
    keys = params.keys()

    if len(keys) == 0:
        return '<h1>Query params</h1><p>No params</p>', 200

    params_table = ''.join([
        f"<tr><td>{key}</td><td>{params[key]}</td></tr>"
        for key in keys
    ])

    response = f'''
    <h1>Query params</h1>
    <table>
        <tr><th>parameter</th><th>value</th></tr>
        {params_table}
    </table>
    '''
    return response, 200


# Task 4
@app.route('/login', methods=['GET', 'POST'])
def login():
    username = ''
    password = ''
    username_error = ''
    password_error = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username and password:
            # Task 8 - Validate form data
            if len(username) < 5:
                # abort(400, 'Invalid username')
                username_error = 'Username at least 5 characters'
            if re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', password) is None:
                # abort(400, 'Invalid password')
                password_error = 'Password must be at least 8 characters and contain at least 1 number and 1 capital letter'

            if username_error == '' and password_error == '':
                # Process user login
                return redirect('/')
        else:
            # Task 4
            abort(400, 'Invalid username or password')

    return f'''
        <form method="POST" action="/login">
            <div>
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" value="{username}"><br>
                <small style="color:red">{username_error}</small>
            </div><br>
            </div>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" value="{password}"><br>
                <small style="color:red">{password_error}</small>
            </div><br><br>
            <div>
                <input type="button" value="Back" onclick="window.location.href='/'">
                <input type="submit" value="Submit">
            </div>
        </form>
        '''


def get_error_content(title, error):
    return f'''
    <h1>{title}</h1><p>{error}</p>
    <input type="button" value="Back" onclick="window.location.href=document.referrer">
    '''


# Task 5
@app.errorhandler(400)
def bad_req_error(error):
    return get_error_content('Bad Request', error), 400


@app.errorhandler(404)
def not_found_error(error):
    return get_error_content('Not Found', error), 404


# Task 5
@app.errorhandler(500)
def server_error(error):
    return get_error_content('Server Error', error), 500


# Task 6
@app.route('/')
def home_page():
    app.logger.info('GET Home page')

    return (
        '<h1>Home Page</h1>'
        '<h3>Tasks 1, 7</h3>'
        '<p>Get random users list: <a href="/users">Users List</a></p>'
        '<p>Get random list of 20 users: <a href="/users?count=20">List of 20 users</a></p>'
        '<p>Get random books list: <a href="/books">Books List</a></p>'
        '<p>Get random list of 20 books: <a href="/books?count=20">List of 20 books</a></p>'
        '<h3>Tasks 2</h3>'
        '<p>Get user with id=1: <a href="/users/1">User 1</a></p>'
        '<p>Get user with id=2: <a href="/users/2">User 2</a></p>'
        '<p>Get book with name: <a href="/books/12">12</a></p>'
        '<p>Get book with name: <a href="/books/kobzaR">"kobzaR"</a></p>'
        '<h3>Tasks 3</h3>'
        '<p>Get params from empty query string: <a href="/params">/params</a></p>'
        '<p>Get params from query string: <a href="/params?name=Test&age=1">/params?name=Test&age=1</a></p>'
        '<h3>Tasks 4</h3>'
        '<p>Login Page: <a href="/login">Login</a></p>'
        '<h3>Tasks 5</h3>'
        '<p>Custom Not Found Page: <a href="/not-found">404</a></p>'
        '<h3>Tasks 6</h3>'
        '<p>Home Page: <a href="/">This page</a></p>'
        '<h3>Tasks 8</h3>'
        '<p>Login form with validation: <a href="/login">Login</a></p>'
    )

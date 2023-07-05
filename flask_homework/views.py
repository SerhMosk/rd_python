# 1. Create html templates for each of the endpoints that were created during
# the execution of the previous DZ. The same data should be displayed, but
# integrated into the templates using context.
# - /users
# - /users/{id}
# - /books
# - /books/{id}
# - /params
# - /login
#
# 2. In the endpoint /login, when filling out the form, add the functionality
# of recording the user name in the session.
#
# 3. Add a check to all pages to see if the session contains a username:
# - If it contains - display the text "Hello, username" at the very beginning
# of the page, where username is the user's name from the session.
# - If it does not contain – redirect the user to the /login page
#
# 4. (optional) Add a logout button to each page, when clicking on which the
# user should be removed from the session and redirected to the /login page.
# For this, you need to implement a separate /logout endpoint as well.
#
# 5. (optional) Add styles to HTML code contained in templates by placing css
# files as static files in a separate directory.

import random
import string
import re
from flask import abort, request, redirect, render_template, session
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


@app.get('/users')
def get_users():
    # Task 3
    if 'username' not in session:
        return redirect('/login')

    filters = request.values
    try:
        cnt = int(filters.get('count')) if filters.get('count') else random.randint(1, 100)
    except ValueError:
        abort(400, 'Invalid count value')

    # ===== generate users
    users = []
    for _ in range(cnt):
        users.append(random.choice(first_names) + ' ' + random.choice(last_names))

    # Task 1
    context = {
        'title': 'User List',
        'users': users,
        'active': 'users'
    }

    return render_template('users/list.html', **context), 200


@app.get('/books')
def get_books():
    if 'username' not in session:
        return redirect('/login')

    filters = request.values
    try:
        cnt = int(filters.get('count')) if filters.get('count') else random.randint(1, 100)
    except ValueError:
        abort(400, 'Invalid count value')

    context = {
        'title': 'Book List',
        'books': generate_random_titles(cnt),
        'active': 'books'
    }

    return render_template('books/list.html', **context), 200


@app.get('/users/<user_id>')
def get_user(user_id):
    if 'username' not in session:
        return redirect('/login')

    try:
        user_id_int = int(user_id)
    except ValueError:
        abort(400, 'Invalid user id')

    if user_id_int % 2 == 0:
        context = {
            'title': 'User Details',
            'user_id': user_id_int,
            'active': 'users'
        }

        return render_template('users/user.html', **context), 200

    abort(404, 'User not found')


@app.get('/books/<name>')
def get_book(name):
    if 'username' not in session:
        return redirect('/login')

    if name.isnumeric():
        abort(400, 'Invalid book name')

    context = {
        'title': 'Book Details',
        'book': name.capitalize(),
        'active': 'books'
    }

    return render_template('books/book.html', **context), 200


@app.get('/params')
def get_params():
    if 'username' not in session:
        return redirect('/login')

    params = request.values
    keys = params.keys()

    context = {
        'title': 'Query params',
        'keys': keys,
        'params': params
    }

    return render_template('params.html', **context), 200


# Task 4
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)

    return redirect('/login')


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
            if len(username) < 5:
                # abort(400, 'Invalid username')
                username_error = 'Username at least 5 characters'
            if re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', password) is None:
                # abort(400, 'Invalid password')
                password_error = 'Password must be at least 8 characters and contain at least 1 number and 1 capital letter'

            if username_error == '' and password_error == '':
                # Task 2
                session['username'] = username

                # Process user login
                return redirect('/')
        else:
            abort(400, 'Invalid username or password')

    context = {
        'username': username,
        'password': password,
        'username_error': username_error,
        'password_error': password_error
    }

    return render_template('auth/login.html', **context), 200


def get_error_content(title, error, page):
    context = {
        'title': title,
        'error': error
    }

    return render_template(page + '.html', **context)


@app.errorhandler(400)
def bad_req_error(error):
    return get_error_content('Bad Request', error, '40x'), 400


@app.errorhandler(404)
def not_found_error(error):
    return get_error_content('Not Found', error, '40x'), 404


@app.errorhandler(500)
def server_error(error):
    return get_error_content('Server Error', error, '50x'), 500


@app.route('/')
def home_page():
    app.logger.info('GET Home page')

    context = {
        'title': 'Home Page',
        'active': '/'
    }

    return render_template('index.html', **context), 200

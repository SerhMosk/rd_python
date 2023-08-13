# 1. Create an .env file, where you add all the data that should be secret:
# - SECRET_KEY
# - Database name (and other details if available)
# - The host and port on which the service is running
# - Other values if necessary
#
# 2. Create a file .env.template, which will describe the structure of .env
# (variable names), but not contain values.
# The .env file DOES NOT need to be pushed to GitHub, the .env.template is required.
# (You can add .env to .gitignore)
#
# 3. Replace all secret values in the code with values from environment
#
# 4. Using flask_sqlalchemy, connect the database and create the following models:
# User,
# book,
# Purchase.
# The data structure and relationships should be the same as in the homework for
# the topic “Basic work with databases. Part 2".
#
# 5. Modify existing or add new endpoints. Display data in JSON format or using an HTML template:
# - GET /user — display a list of all User objects (all records of the corresponding table)
# - GET /user/<int:user_id> — display information about the User with the corresponding id, or 404
# - GET /book — display a list of all Book objects (all records of the corresponding table)
# - GET /book/<int:book_id> — display information about the Book with the corresponding id, or 404
# - GET /purchase — display a list of all Purchase objects (all records of the corresponding table)
# - GET /purchase/<int:purchase_id> — display information about the Purchase with the corresponding id, or 404
#
# 6. (optional) When transmitting with query param size=n for endpoints with a list
# of objects, show the corresponding number of objects.
#
# 7. (optional) When requesting endpoints /purchase and /purchase/<int:purchase_id>,
# display not only information about purchase, but also the name of the book and
# the name of the user who bought it.
#
# 8. (optional) Implement the possibility of creating new objects in the database.
# Endpoints can accept "application/json" or "application/x-www-form-urlencoded":
# - POST /user
# - POST /book
# - POST /purchase (check if the corresponding User and Book exist)

import re
from flask import abort, request, redirect, render_template, session, url_for
from sqlalchemy import desc, or_, and_, func
from app import app, db
from models import User, Book, Purchase


def get_list(query):
    result = db.session.execute(query).scalars()
    return [item.__dict__ for item in result]


# Task 5
@app.get('/users')
def user_list():
    if 'username' not in session:
        return redirect(url_for('login'))

    filters = request.values
    # Task 6
    try:
        cnt = int(filters.get('size')) if filters.get('size') else None
    except ValueError:
        abort(400, 'Invalid size value')

    columns = ['id', 'username', 'first_name', 'last_name', 'age']
    query = db.select(User).limit(cnt) if cnt else db.select(User)
    users = get_list(query)

    context = {
        'title': 'User List',
        'active': 'users',
        'users': users,
        'keys': columns
    }

    return render_template('user/list.html', **context), 200


# Task 5
@app.get('/users/<user_id>')
def user_detail(user_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    user = db.get_or_404(User, user_id)

    context = {
        'title': 'User Details',
        'active': 'users',
        'user': user.__dict__
    }

    return render_template('user/detail.html', **context), 200


# Task 8
@app.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        data = request.form

        query = db.select(User).filter(or_(
            User.username == data["username"],
            User.first_name == data["first_name"],
            User.last_name == data["last_name"]
        ))
        users = get_list(query)

        if len(users):
            return 'Username, first name or last name is not unique', 409

        user = User(
            username=data["username"],
            password=data["password"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            age=data["age"],
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('user_detail', user_id=user.id))

    context = {
        'title': 'Create User',
        'active': 'users'
    }

    return render_template("user/create.html", **context)


# Task 8: additional
@app.delete("/users/<int:user_id>")
def user_delete(user_id):
    user = db.get_or_404(User, user_id)

    db.session.delete(user)
    db.session.commit()

    # return redirect(url_for("user_list"))
    return 'OK', 200


@app.get('/books')
def book_list():
    if 'username' not in session:
        return redirect(url_for('login'))

    filters = request.values
    try:
        cnt = int(filters.get('size')) if filters.get('size') else None
    except ValueError:
        abort(400, 'Invalid size value')

    columns = ['id', 'title', 'author', 'year', 'price']
    query = db.select(Book).limit(cnt) if cnt else db.select(Book)
    books = get_list(query)

    context = {
        'title': 'Book List',
        'active': 'books',
        'books': books,
        'keys': columns
    }

    return render_template('book/list.html', **context), 200


@app.get('/books/<book_id>')
def book_detail(book_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    book = db.get_or_404(Book, book_id)

    context = {
        'title': 'Book Details',
        'active': 'books',
        'book': book.__dict__
    }

    return render_template('book/detail.html', **context), 200


@app.route("/books/create", methods=["GET", "POST"])
def book_create():
    if request.method == "POST":
        data = request.form

        query = db.select(Book).filter(and_(
            Book.title == data["title"],
            Book.author == data["author"],
            Book.year == data["year"]
        ))
        books = get_list(query)

        if len(books):
            return 'The book was added earlier', 409

        book = Book(
            title=data["title"],
            author=data["author"],
            year=data["year"],
            price=data["price"],
        )

        db.session.add(book)
        db.session.commit()

        return redirect(url_for('book_detail', book_id=book.id))

    context = {
        'title': 'Create Book',
        'active': 'books'
    }

    return render_template("book/create.html", **context)


@app.delete("/books/<int:book_id>")
def book_delete(book_id):
    book = db.get_or_404(Book, book_id)

    db.session.delete(book)
    db.session.commit()

    # return redirect(url_for("book_list"))
    return 'OK', 200


@app.get('/purchases')
def purchase_list():
    if 'username' not in session:
        return redirect(url_for('login'))

    filters = request.values
    try:
        cnt = int(filters.get('size')) if filters.get('size') else None
    except ValueError:
        abort(400, 'Invalid size value')

    columns = ['id', 'book', 'username', 'price', 'date']

    # First solution
    # query = db.session
    #     .query(Purchase.id, Book.id, Book.title, User.id, User.username, Purchase.date).join(Book).join(User)\
    #     .limit(cnt if cnt else -1)

    # Second solution
    if cnt:
        query = db.session.query(Purchase, Book, User).join(Book).join(User).limit(cnt)
    else:
        query = db.session.query(Purchase, Book, User).join(Book).join(User)
    purchases = query.all()

    # Task 7
    books = get_list(db.select(Book))
    users = get_list(db.select(User))

    context = {
        'title': 'Purchase List',
        'active': 'purchases',
        'purchases': purchases,
        'keys': columns,
        'books': books,
        'users': users
    }

    return render_template('purchase/list.html', **context), 200


@app.get('/purchases/<purchase_id>')
def purchase_detail(purchase_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    # Task 7
    result = db.get_or_404(Purchase, purchase_id)
    query = db.session.query(Purchase, Book, User).join(Book).join(User).filter(Purchase.id == purchase_id).limit(1)
    context = {
        'title': 'Purchase Details',
        'active': 'purchases',
        'purchase': query.all()
    }

    return render_template('purchase/detail.html', **context), 200


@app.route("/purchases/create", methods=["GET", "POST"])
def purchase_create():
    if request.method == "POST":
        data = request.form

        if data['book_id'] is None or data['user_id'] is None:
            return 'Invalid book_id or user_id value', 400

        try:
            book_id = int(data['book_id']) if data['book_id'] else 0
            user_id = int(data['user_id']) if data['user_id'] else 0
        except ValueError:
            return 'Invalid book_id or user_id value', 400

        purchase = Purchase(
            book_id=book_id,
            user_id=user_id,
        )

        db.session.add(purchase)
        db.session.commit()

        return redirect(url_for('purchase_detail', purchase_id=purchase.id))

    books = get_list(db.select(Book))
    users = get_list(db.select(User))

    context = {
        'title': 'Create Purchase',
        'active': 'purchases',
        'books': books,
        'users': users
    }

    return render_template("purchase/create.html", **context)


@app.delete("/purchases/<int:purchase_id>")
def purchase_delete(purchase_id):
    purchase = db.get_or_404(Purchase, purchase_id)

    db.session.delete(purchase)
    db.session.commit()

    # return redirect(url_for("book_list"))
    return 'OK', 200


@app.get('/params')
def param_list():
    if 'username' not in session:
        return redirect(url_for('login'))

    params = request.values

    context = {
        'title': 'Query params',
        'keys': params.keys(),
        'params': params
    }

    return render_template('params.html', **context), 200


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)

    return redirect(url_for('login'))


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
                session['username'] = username

                # Process user login
                return redirect(url_for('home_page'))
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


@app.errorhandler(405)
def not_allowed(error):
    return get_error_content('Not Allowed', error, '40x'), 405


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

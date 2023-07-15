### Lesson 36: Introduction to Django

1. Create a separate django directory in the homework repository.
2. In the django directory, create a virtualenv, activate it and install Django.
3. Create a Django project using django-admin.
4. Create an .env where all sensitive values from the settings can be exported.
   - In settings, use environment variables, not "raw" values.
   - Use the python_dotenv library
5. Create a requirements.txt file, which should contain information about the installed packages of your virtual environment.

    The directory with the virtual environment, the database file, and the .env file should not be uploaded to the repository. To do this, you can add them to .gitignore.
6. Create an application user
7. Create a view that should be available under /users and return the text "Hello, users!"
8. Apply standard migrations for the project.
9. Create a superadmin to access the django admin panel (http://localhost:8000/admin)

### Lesson 37: Object-relational projection on Django

1. Create Django applications: user, book, purchase. Add information about these apps to INSTALLED_APPS (settings.py)
2. Create User, Book, Purchase models in the relevant applications. The structure and relationships of the tables should be the same as in the previous homework.
3. Create the necessary migrations
4. Create the simplest views for each application. Each of them should return all the records from the corresponding table in the database in json format.
 
    Create the appropriate settings urls:
   - GET users/
   - GET books/
   - GET purchases/

5. (optional) Modify the models as follows:
   - In Book title and author together must be unique. That is, there cannot be 2 identical books for the same author.
   - In Purchase, change the sorting order to sort by date in descending order.

    Separate migrations must be created for these modifications, in addition to those created in Task 3.
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

### Lesson 38: Working with Django. Part 1

1. For existing models, create a configuration for display in Django Admin. Tables in Django Admin should display all object attributes.
2. Redefine the str method of existing models, giving object names a more readable appearance. For example, instead of displaying "User object(1)" it should display "1: Test User"

### Lesson 39: Working with Django. Part 2

1. For each existing model, replace the simplest view functions with classes (class based views), register the corresponding urls.
   - For each model, the functionality of obtaining a list of objects (for example, GET /users) and obtaining one object by id (for example, GET /users/<int:id>) should be implemented.
   - The data must be rendered using HTML templates.
2. Implement the functionality of creating new objects by creating the corresponding views and registering the corresponding urls.
Create appropriate forms to be used to create objects.

### Lesson 40: Django REST (DRF). Part 1

1. Install the Django REST Framework to the existing Django project and update the settings accordingly.
2. Create appropriate Serializers for all existing models.

### Lesson 41: Django REST (DRF). Part 2

1. For all models, create a ViewSet by adding previously created serializers to them. Create appropriate routers.
2. Configure standard pagination at the project level. Display 5 elements per page.
3. Redefine pagination for UserViewSet, where 10 elements are displayed per page. All other ViewSets should display 5 elements each.
4. Configure filtering for all ViewSets at the project level. For each ViewSet, define fields that can be sorted and searched.

### Lesson 42: Asynchronous tasks in Django

1. Install and configure celery for your django project.
Install auxiliary libraries for working with task broker (redis, rabbitmq).
2. Freeze all installed libraries in the requirements.txt file: pip freeze > requirements.txt
3. Inside the application user, create a celery task that will print any text.
4. Inside the user application, create a celery task that will accept the user_id parameter and print the number of purchases for this user.
5. Inside the user application, create a scheduled celery task that will print the number of user objects in the database every minute.

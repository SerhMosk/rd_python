import os
from dotenv import load_dotenv


# Task 3
class AppConfig:
    load_dotenv()

    DEBUG = os.getenv('DEBUG')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

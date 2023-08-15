"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import dj_database_url

from django.core.exceptions import ImproperlyConfigured
from pathlib import Path

from django.core.management.commands.runserver import Command as runserver


def get_env_value(env_variable):
    try:
        if env_variable == 'ALLOWED_HOSTS':
            return os.environ[env_variable].split(', ')
        if env_variable in ['DEBUG', 'USE_I18N', 'USE_TZ']:
            return os.environ[env_variable].lower() in ['true', '1', 'yes']
        return os.environ[env_variable]
    except KeyError:
        error_msg = f'Set the {env_variable} environment variable'
        raise ImproperlyConfigured(error_msg)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_value('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_value('DEBUG')

ALLOWED_HOSTS = get_env_value('ALLOWED_HOSTS')

runserver.default_port = get_env_value('DEFAULT_PORT')
runserver.default_addr = get_env_value('DEFAULT_HOST')
runserver.protocol = get_env_value('PROTOCOL')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'django_celery_beat',
    'bootstrap5',
    'widget_tweaks',
    'user.apps.UserConfig',
    'book.apps.BookConfig',
    'purchase.apps.PurchaseConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

OPTIONS = {
    'sql_mode': 'traditional',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': get_env_value("DB_HOST"),   # Or an IP Address that your DB is hosted on
        'PORT': get_env_value("DB_PORT"),
        'NAME': get_env_value("DB_NAME"),
        'USER': get_env_value("DB_USER"),
        'PASSWORD': get_env_value("DB_PASSWORD"),
    }
    # 'default': dj_database_url.config(
    #     conn_max_age=600,
    #     conn_health_checks=True,
    # )
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / get_env_value("DATABASE_URL"),
    # }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = get_env_value("LANGUAGE_CODE")

TIME_ZONE = get_env_value("TIME_ZONE")

USE_I18N = get_env_value("USE_I18N")

USE_TZ = get_env_value("USE_TZ")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = get_env_value("STATIC_URL")
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / get_env_value("STATIC_URL"),
]
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user.User'

# Config for DRF
# https://www.django-rest-framework.org/api-guide/settings/#settings
# Look into settings in python shell
# > from rest_framework.settings import api_settings
# > api_settings.defaults
REST_FRAMEWORK = {
    'PAGE_SIZE': 5,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ]
}

# Celery settings
CELERY_BROKER_URL = get_env_value("REDIS_URL")
CELERY_RESULT_BACKEND = get_env_value("REDIS_URL")

# Celery beat tasks
# CELERY_BEAT_SCHEDULE = {
#     'print_user_number_every_minute': {  # A unique name for this task
#         'task': 'user.tasks.print_user_number',  # Import path for the task
#         'schedule': 60.0,  # Run every minute
#     },
# }

CSRF_TRUSTED_ORIGINS = ["http://localhost"]

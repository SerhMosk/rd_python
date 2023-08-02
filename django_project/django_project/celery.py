import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

app = Celery('django_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Celery beat tasks
app.conf.beat_schedule = {
    'print_user_number_every_minute': {
        'task': 'user.tasks.print_user_number',  # the task to be performed
        'schedule': 60,  # frequency with which to perform the task (in seconds), or crontab
        'args': (),  # positional arguments
        'kwargs': {},  # named arguments
    }
}

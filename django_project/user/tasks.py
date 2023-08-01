from celery import shared_task

from purchase.models import Purchase
from user.models import User


@shared_task
def print_hello():
    print("Hello from users app")


@shared_task
def print_user_purchases_number(user_id):
    purchases_number = Purchase.objects.filter(user__id=user_id).count()
    print(f"User with id={user_id} has {purchases_number} purchase(s)")


@shared_task
def print_user_number():
    users_number = User.objects.count()
    print(f"In this app registered {users_number} user(s)")
from django.shortcuts import render

from book.models import Book
from purchase.models import Purchase
from user.models import User


def index(request):
    num_books = Book.objects.count()
    num_users = User.objects.count()
    num_purchases = Purchase.objects.count()

    context = {
        'title': 'Home Page',
        'active': '/',
        'num_books': num_books,
        'num_users': num_users,
        'num_purchases': num_purchases,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

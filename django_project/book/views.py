# import json
#
# from django.core import serializers
# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from book.models import Book


def books_view(request):
    books = list(Book.objects.all().values())

    return JsonResponse({'data': books})

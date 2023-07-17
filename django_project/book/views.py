# import json
#
# from django.core import serializers
# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from book.models import Book


def books_view(request):
    books = list(Book.objects.all().values())
    # records = Book.objects.all()
    # books = serializers.serialize('json', records)
    # struct = json.loads(data)
    # books = json.dumps(struct)
    # print(books)

    # return HttpResponse(books, content_type='application/json')
    return JsonResponse({'data': books})

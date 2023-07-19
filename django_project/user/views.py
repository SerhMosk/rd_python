# import json
#
# from django.core import serializers
# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from user.models import User


def users_view(request):
    users = list(User.objects.all().values())

    return JsonResponse({'data': users})

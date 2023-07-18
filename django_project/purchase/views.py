# import json
#
# from django.core import serializers
# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from purchase.models import Purchase


def purchases_view(request):
    purchases = list(Purchase.objects.all().values())

    return JsonResponse({'data': purchases})

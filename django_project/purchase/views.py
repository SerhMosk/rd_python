# import json
#
# from django.core import serializers
# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from purchase.models import Purchase


def purchases_view(request):
    purchases = list(Purchase.objects.all().values())
    # records = Purchase.objects.all()
    # data = serializers.serialize('json', records)
    # struct = json.loads(data)
    # purchases = json.dumps(struct)
    # print(purchases)

    # return HttpResponse(purchases, content_type='application/json')
    return JsonResponse({'data': purchases})

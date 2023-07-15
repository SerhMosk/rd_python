# import json
#
# from django.core import serializers
# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from user.models import User


def users_view(request):
    users = list(User.objects.all().values())
    # records = User.objects.all()
    # data = serializers.serialize('json', records)
    # struct = json.loads(data)
    # users = json.dumps(struct)
    # print(users)

    # return HttpResponse(users, content_type='application/json')
    return JsonResponse({'data': users})

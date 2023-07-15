from django.urls import path

from . import views

urlpatterns = [
    path('', views.purchases_view, name='index'),
]
from django.urls import path

from api import views
from api.user.urls import urlpatterns as user_urls
from api.book.urls import urlpatterns as book_urls
from api.purchase.urls import urlpatterns as purchase_urls

app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
] + user_urls + book_urls + purchase_urls

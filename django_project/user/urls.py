from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('list', views.user_list, name='user-list'),
    path('add', views.user_add, name='user-add'),
    path('<int:pk>/edit', views.user_edit, name='user-edit'),
    path('<int:pk>/remove', views.user_remove, name='user-remove'),
    path('', views.UserListView.as_view(), name='user-index'),
    path('create/', views.UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/update', views.UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/delete', views.UserDeleteView.as_view(), name='user-delete'),
]
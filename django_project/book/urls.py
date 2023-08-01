from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('list', views.book_list, name='book-list'),
    path('add', views.book_add, name='book-add'),
    path('<int:pk>/edit', views.book_edit, name='book-edit'),
    path('<int:pk>/remove', views.book_remove, name='book-remove'),
    path('', views.BookListView.as_view(), name='book-index'),
    path('create/', views.BookCreateView.as_view(), name='book-create'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('<int:pk>/update', views.BookUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete', views.BookDeleteView.as_view(), name='book-delete'),
]

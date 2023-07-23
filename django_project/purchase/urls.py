from django.urls import path

from . import views

app_name = 'purchases'

urlpatterns = [
    path('list', views.purchase_list, name='purchase-list'),
    path('add', views.purchase_add, name='purchase-add'),
    path('<int:pk>/edit', views.purchase_edit, name='purchase-edit'),
    path('<int:pk>/remove', views.purchase_remove, name='purchase-remove'),
    path('', views.PurchaseListView.as_view(), name='purchase-index'),
    path('create/', views.PurchaseCreateView.as_view(), name='purchase-create'),
    path('<int:pk>/', views.PurchaseDetailView.as_view(), name='purchase-detail'),
    path('<int:pk>/update', views.PurchaseUpdateView.as_view(), name='purchase-update'),
    path('<int:pk>/delete', views.PurchaseDeleteView.as_view(), name='purchase-delete'),
]
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.ItemDetailView, name='item_detail'),
    path('', views.ItemsListView, name='items_list')
]

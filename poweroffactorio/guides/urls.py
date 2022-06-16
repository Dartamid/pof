from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.GuideDetailView, name='guide_detail'),
    path('', views.GuidesListView, name='guides_list'),
]
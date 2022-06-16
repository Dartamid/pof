from django.urls import path
from . import views


urlpatterns = [
    path('about-us/', views.AboutUsPageView, name='about-us'),
    path('', views.TitlePageView, name='title_page'),
]
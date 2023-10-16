from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.camping_search_form, name='camping_search_form'),
    path('search/', views.search_camping_sites, name='search_camping_sites'),
]
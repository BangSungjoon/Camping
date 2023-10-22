from django.urls import path
from . import views
from .views import CampImagesDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('camping/list/', views.camping_list, name='camping_list'),
    path('camping/detail/<str:camp_no>/', views.camping_detail, name='camping_detail'),
    path('camping/insert/', views.camping_insert, name='camping_form'),
    path('camp_images/<int:pk>/', CampImagesDetailView.as_view(), name='camp_images_detail'),
    path('camping/safety/', views.camping_safety, name='camping_safety'),
    path('detail/', views.detail, name='detail'),
    path('camping/search/location', views.camping_search_location, name='camping_search_location'),
    path('get_detail_intro/', views.get_detail_intro, name='get_detail_intro'),
    path('camping/detail/<str:camp_no>/detail_intro.html', views.detail_intro, name='detail_intro'),
]
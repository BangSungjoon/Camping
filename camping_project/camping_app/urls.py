from django.urls import path, re_path
from . import views
from .views import CampImagesDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('camping/list/', views.camping_list, name='camping_list'),
    path('camping/camping_detail/<str:camp_no>/', views.camping_detail, name='camping_detail'),
    path('camping/insert/', views.camping_insert, name='camping_form'),
    path('camp_images/<int:pk>/', CampImagesDetailView.as_view(), name='camp_images_detail'),
    path('camping/safety/', views.camping_safety, name='camping_safety'),
    path('camping/search/location', views.camping_search_location, name='camping_search_location'),
    # path('camping/search/result/', views.camping_search, name='camping_search'),
    re_path(r'^camping/search_result/(?P<keyword>[\wㄱ-ㅎㅏ-ㅣ가-힣]+)?/(?P<c_do>[\wㄱ-ㅎㅏ-ㅣ가-힣]+)?/(?P<c_signgu>[\wㄱ-ㅎㅏ-ㅣ가-힣]+)?/?$', views.camping_search, name='camping_search'),
    # path('camping/search/result/', views.camping_search_result, name='camping_search_result'),
    path('get_detail_intro/', views.get_detail_intro, name='get_detail_intro'),
    path('camping/detail_intro/', views.detail_intro, name='detail_intro'),
]
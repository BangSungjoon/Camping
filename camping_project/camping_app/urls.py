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
    re_path(r'^camping/search_result/(?P<keyword>[\wㄱ-ㅎㅏ-ㅣ가-힣]+)?/(?P<c_do>[\wㄱ-ㅎㅏ-ㅣ가-힣]+)?/(?P<theme>[\wㄱ-ㅎㅏ-ㅣ가-힣]+)?/?$', views.camping_search, name='camping_search'),
    # path('camping/search/result/', views.camping_search_result, name='camping_search_result'),
    path('camping/detail_intro/<int:camp_no>', views.detail_intro, name='detail_intro'),
    path('camping/detail_text/<int:camp_no>', views.detail_text, name='detail_text'),
    path('camping/detail_review/<int:camp_no>', views.detail_review, name='detail_review'),
    path('camping/detail_weather/', views.detail_weather, name='detail_weather'),
    path('camping/detail_map/<int:camp_no>', views.detail_map, name='detail_map'),
    path('camping/book/<str:camp_no>/' , views.camping_book, name='camping_book'),
    path('camping/review/<str:camp_no>/' , views.camping_review, name='camping_review'),
    path('camping/secondhanded/', views.camping_secondhanded, name='camping_secondhanded'),
    path('camping/camping_new_list/', views.camping_new_list, name='camping_new_list'),
    path('camping/camping_new_detail/<str:camp_no>', views.camping_new_detail, name='camping_new_detail'),
]
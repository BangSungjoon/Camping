from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign_in', auth_views.LoginView.as_view(template_name='users_app/sign_in.html') , name='sign_in'),
    path('sign_out', views.sign_out, name='sign_out'),
    
    path('sign_up/user/', views.sign_up_user, name='sign_up'),  # 이 URL 패턴을 추가
    path('', views.sign_up_user, name='sign_up_user'),  # 이 URL 패턴도 같은 뷰를 가리키게 설정
        
    path('sign_up/business', views.sign_up2, name='sign_up2'),
    path('sign_up/select', views.sign_up_select, name='sign_up_select'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),



# mypage
    path('user/mypage', views.user_mypage, name='user_mypage'),
    
    path('user/mypage/1', views.user_info_profile_render, name='user_info_profile'),
    path('user/mypage/2', views.user_review_list_render, name='user_review_list'),
    path('user/mypage/3', views.user_favorite_list_render, name='user_favorite_list'),
    path('user/mypage/4', views.user_inquiry_list_render, name='user_inquiry_list'),
    
    path('user/mypage/1', views.user_info_profile, name='user_info_edit'),
    path('user/mypage/2', views.user_review_list, name='user_review_list'),
    path('user/mypage/3', views.user_favorite_list, name='user_favorite_list'),
    path('user/mypage/4', views.user_inquiry_list, name='user_inquiry_list'),

    path('user/mypage/3/delete/<str:prd_no>/', views.user_favorite_delete, name='user_favorite_delete'),


    path('user/inquire', views.user_inquire, name='user_inquire'),
]


from django.urls import path
# from django.urls import include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('camping/', include('camping_app.urls')),  # camping_app의 URL 패턴을 include합니다.

    # path('sign_in', auth_views.LoginView.as_view(template_name='users_app/sign_in.html') , name='sign_in'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_out', views.sign_out, name='sign_out'),
    # 회원가입
    path('sign_up/user/', views.sign_up, name='sign_up_user'), 
    path('', views.sign_up_user, name='sign_up_user'),
    path('sign_up/select', views.sign_up_select, name='sign_up_select'),

    
    # 기업전환 : name='sign_up2_company'중복됨
    # path('sign_up/company', views.sign_up2, name='sign_up2_company'),
    path('sign_up/company', views.sign_up2, name='sign_up'),
    path('sign_up/sign_up2_company', views.sign_up2_company, name='sign_up2_company'),

    # mypage
    path('user/mypage', views.camp_register, name='user_mypage'),
    path('user/mypage/1', views.user_booked, name='user_booked'),
    path('user/mypage/2', views.user_review_list, name='user_review_list'),
    path('user/mypage/3', views.user_favorite_list, name='user_favorite_list'),
    path('user/mypage/4', views.user_inquiry_list, name='user_inquiry_list'),
    path('user/mypage/5', views.sign_up2, name='sign_up2'),



    path('user/mypage/1/delete/<str:book_no>/', views.user_booked_delete, name='user_booked_delete'),
    path('user/mypage/3/delete/<str:fav_id>/', views.user_favorite_delete, name='user_favorite_delete'),
    path('user/mypage/2/update/<str:review_no>/', views.user_review_update, name='user_review_update'),
    path('user/mypage/2/delete/<str:review_no>/', views.user_review_delete, name='user_review_delete'),
    path('user/mypage/delete/<str:camp_no>/', views.camp_register_delete, name='camp_register_delete'),

    path('user/inquire', views.user_inquire, name='user_inquire'),
    path('users/user/inquire/rep/<int:inq_no>/', views.user_inquiry_rep, name='user_inquiry_rep'),
]


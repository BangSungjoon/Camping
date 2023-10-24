from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # pass # 기본 auth_user 테이블과 동일
    # id(넘버), password(비번), username(로그인시 아이디), email(이메일)은 내장필드임
    # 새로운 필드 추가 
    user_name = models.CharField(max_length=30) #개인이름
    user_age = models.IntegerField(null=True, blank=True) #나이
    user_gender = models.IntegerField(null=True, choices=((1, '남성'), (2, '여성'))) #성별
    user_tel = models.CharField(max_length=20) #전화번호(공통)
    user_address = models.CharField(null=True, blank=True, max_length=200) #주소(공통)
    
    user_subscribe_sms = models.BooleanField(default=False) #메일링(공통)
    user_subscribe_email = models.BooleanField(default=False) #메일링(공통)

#  User 상속 받음 :
# CompanyUser 별도로 생성됨 
# 기본키 : usr_ptr_id (User 테이블을 참조하는 외래키가 됨)
class CompanyUser(User):
    # class Meta :  
    #     proxy = True
    
    # 새로운 필드 추가 
    company_name = models.CharField(max_length=30) #회사명
    company_tel = models.CharField(max_length=20) #회사전번
    company_address = models.CharField(max_length=200) #회사위치
    class Meta:
        managed = True
        
# Create your models here.
# class User(AbstractUser):
#     # pass # 기본 auth_user 테이블과 동일
    
#     # 새로운 필드 추가 
#     user_name = models.CharField(max_length=30)
#     user_phone = models.CharField(max_length=20)
#     user_address = models.CharField(max_length=200)

# #  User 상속 받음 :
# # CompanyUser 별도로 생성됨 
# # 기본키 : usr_ptr_id (User 테이블을 참조하는 외래키가 됨)
# class CompanyUser(User):
#     # class Meta :  
#     #     proxy = True
    
#     # 새로운 필드 추가 
#     camp_id = models.CharField(max_length=30)
#     camp_name = models.CharField(max_length=30)
#     camp_phone = models.CharField(max_length=20)
#     camp_address = models.CharField(max_length=200)
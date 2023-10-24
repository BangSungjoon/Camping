from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

from django.http import JsonResponse
from django.core import serializers

from .models import User
from .models import CompanyUser
from .forms import SignUpForm, CompanyUserForm, UserProfileForm
from django import forms

from camping_app.models import CampInfo, FavoriteList, CampReview, UserInquire, InqReply


from django.contrib.auth.decorators import login_required



# Create your views here.

#로그인
def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
        
    else:
        messages.error(request, '로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요.')
        form = AuthenticationForm()
    return render(request, 'users_app/sign_in.html', {'form':form})
    
    
# 로그아웃
def sign_out(request):
    logout(request)
    return redirect('index')

# 회원가입

def sign_up_select(request):
    return render(request, 'users_app/sign_up_select.html')

def sign_up(request):
    return render(request, 'users_app/sign_up.html')

def sign_up_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_name = request.POST['user_name']
        user_age = request.POST['user_age']
        user_gender = request.POST['user_gender']
        user_tel = request.POST['user_tel']
        user_address = request.POST['user_address']
        email = request.POST['email']
        user_subscribe_sms = request.POST.get('user_subscribe_sms') == 'on'
        user_subscribe_email = request.POST.get('user_subscribe_email') == 'on'

        if not username or not password or not email or not user_name or not user_gender or not user_tel:
            # 필수 필드 중 하나라도 비어 있는 경우 오류 메시지 설정
            messages.error(request, "필수 항목을 입력해주세요.")
            return render(request, 'sign_up.html')   # 회원가입 양식 페이지로 리디렉션
        # 매개변수는 3개만 전달 가능
        # 순서 주의 : username, email, password 
        
        user_age = request.POST.get('user_age')
        if not user_age:
            user_age = None
        else:
            # user_age가 빈 문자열이 아닌 경우, 숫자로 변환
            try:
                user_age = int(user_age)
            except ValueError:
                messages.error(request, "오류가 발생하였습니다.")

                
        user = User.objects.create_user(username, email, password)
        user.user_name = user_name
        user.user_age = user_age
        user.user_gender = user_gender
        user.user_tel = user_tel
        user.user_address = user_address
        user.user_subscribe_sms = user_subscribe_sms
        user.user_subscribe_email = user_subscribe_email
        
        user.save()
        messages.success(request, "캠핑어때의 회원이 되신 것을 환영합니다!")

        return redirect('sign_in') # 회원가입 후 로그인화면으로 이동

    return render(request, 'users_app/sign_up.html')

# def sign_up_user(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()  # 데이터 저장
#             return JsonResponse({'success': True})
#         else:
#             errors = form.errors
#             return JsonResponse({'success': False, 'errors': errors})
#     else:
#         form = SignUpForm()

#     return render(request, 'users_app/sign_up.html', {'form': form})
#     # return JsonResponse({'success': True})


def sign_up2(request):
    return render(request, 'users_app/sign_up2.html')

# def sign_up2_company(request):
#     if request.method == 'POST':
#         company_name = request.POST['company_name']
#         company_tel = request.POST['company_tel']
#         company_address = request.POST['company_address']

#         if not company_name or not company_tel or not company_address:
#             # 필수 필드 중 하나라도 비어 있는 경우 오류 메시지 설정
#             messages.error(request, "필수 항목을 입력해주세요.")
#             return render(request, 'sign_up2.html')   # 회원가입 양식 페이지로 리디렉션
#         # 매개변수는 3개만 전달 가능
#         # 순서 주의 : username, email, password 
#         CompanyUser = CompanyUser.objects.create_user(company_name, company_tel, company_address)
#         CompanyUser.company_name = company_name
#         CompanyUser.company_tel = company_tel
#         CompanyUser.company_address = company_address
        
#         CompanyUser.save()
#         messages.success(request, "기업회원 전환을 환영합니다!")

#         return redirect('user_mypage') # 회원가입 후 로그인화면으로 이동

#     return render(request, 'users_app/user_mypage.html') 

def sign_up2_company(request):
    if request.method == 'POST':
        user_instance = request.user

        form = CompanyUserForm(request.POST, user_instance=user_instance)
        if form.is_valid():
            # 폼 데이터 처리
            company_user = form.save(commit=False)
            company_user.user_instance = user_instance  # 외래키 필드 설정
            company_user.save()
            # 나머지 처리 및 리디렉션

    else:
        form = CompanyUserForm(user_instance=request.user)  # 폼 초기화

    return render(request, 'user_mypage.html', {'form': form})



# 문의
    
def user_inquire(request):
    return render(request, 'users_app/user_inquire.html')

# 마이페이지

def user_mypage(request):
    return render(request, 'users_app/user_mypage.html')


# 정보수정
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # 정보 업데이트 성공 시 어떤 페이지로 이동하도록 설정
            return redirect('user_info_profile')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'user_info_profile.html', {'user': user, 'form': form})


# ajax

def user_info_profile_render(request):
    return render(request, 'users_app/user_info_profile.html')

def user_info_profile(request):
    template_name = 'users_app/user_info_profile.html'
    rendered_template = render(request, template_name)
    response_data = {
        'html': rendered_template.content.decode('utf-8')
    }

    return JsonResponse(response_data)

def user_profile(request):
    user = request.user  # 현재 로그인한 사용자 정보를 얻습니다.
    return render(request, 'profile.html', {'user': user})

def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # 정보 업데이트 성공 시 어떤 페이지로 이동하도록 설정
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})


# favorite

def user_favorite_list_render(request):
    return render(request, 'users_app/user_favorite_list.html')

# def user_favorite_list(request):
#     template_name = 'users_app/user_favorite_list.html'
#     rendered_template = render(request, template_name)
#     response_data = {
#         'html': rendered_template.content.decode('utf-8')
#     }

#     return JsonResponse(response_data)



def user_favorite_list(request):
    user_favorite_campings = FavoriteList.objects.select_related('camp_no').filter(id=request.user.id)
    return render(request, 'your_template.html', {'user_favorite_campings': user_favorite_campings})

# def user_favorite_list(request, camp_no):
#     현재 로그인한 사용자에 대한 FavoriteList 데이터 가져오기
#     camp_no = CampInfo.objects.all()
#     user_favorite_campings = FavoriteList.objects.filter(id=request.user.id)
    
#     return render(request, 'users_app/user_favorite_list.html', {'user_favorite_campings': user_favorite_campings})


def user_favorite_delete(request, camp_no):
    # prd_no에 해당되는 상품 찾아와서
    Favorite = get_object_or_404(FavoriteList, pk=camp_no)

    # 상품 데이터 삭제
    Favorite.delete()

    # 상품 조회 화면으로 이동 (포워딩)
    return redirect('user_favorite_list')
    
    # review

def user_review_list_render(request):
    return render(request, 'users_app/user_review_list.html')

# def user_review_list(request):
#     template_name = 'users_app/user_review_list.html'
#     rendered_template = render(request, template_name)
#     response_data = {
#         'html': rendered_template.content.decode('utf-8')
#     }

#     return JsonResponse(response_data)

def user_review_list(request):
    user_reviews = CampReview.objects.filter(id=request.user.id)
    
    return render(request, 'users_app/user_review.html', {'user_reviews': user_reviews})

    

# inquiry

def user_inquiry_list_render(request):
    return render(request, 'users_app/user_inquiry_list.html')

# def user_inquiry_list(request):
#     template_name = 'users_app/user_inquiry_list.html'
#     rendered_template = render(request, template_name)
#     response_data = {
#         'html': rendered_template.content.decode('utf-8')
#     }

#     return JsonResponse(response_data)

def user_inquiry_list(request):
    user_inquiries = UserInquire.objects.filter(id=request.user.id)
    
    return render(request, 'users_app/user_inquiry.html', {'user_inquiries': user_inquiries})

def user_inquiry_rep(request, inq_no):
    inquiry = get_object_or_404(UserInquire, inq_no=inq_no)
    reply = InqReply.objects.filter(inq_no=inquiry)
    
    return render(request, 'users_app/user_inquiry_rep.html', {'inquiry': inquiry, 'reply':reply})

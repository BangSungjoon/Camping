from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

from django.http import JsonResponse
from django.core import serializers

from camping_app.review_from import campreviewform

from .models import User, UsersAppCompanyuser
# from .models import UsersAppCompanyuser
# from .forms import SignUpForm
from .forms2 import CompanyUserForm, InquireForm
# from django import forms

from camping_app.models import CampMemeberInfo, FavoriteList, CampReview, ImageLink, UserInquire, InqReply, Booking

from django.contrib.auth.decorators import login_required

from django.db.models import Q
import datetime
# Create your views here.

#로그인
def sign_in(request):
    print("aa")
    if request.method == 'POST':
        print(request.POST)
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
        
    else:
        # messages.error(request, '로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요.')
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
                messages.error(request, "추가 정보를 입력하고 혜택을 받으세요.")

                
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


def sign_up2(request):
    return render(request, 'users_app/sign_up2.html')

def sign_up2_company(request):
    print('aa')
    
    if request.method == 'POST':
        
        # user_instance = request.user
        # user_ptr_id=request.POST["user_ptr_id"]
        # company_name=request.POST["company_name"]
        # company_tel=request.POST["company_tel"]
        # company_address=request.POST["company_address"]
        
        # print(id,company_name, company_tel, company_address)
        # print(request.POST)

        form = CompanyUserForm(request.POST)
        if form.is_valid():            
            company = form.save(commit=False)
            company.save()
            return redirect('user_mypage')       
       
    else:
        # form = CompanyUserForm(user_instance=request.user)  # 폼 초기화
        form = CompanyUserForm()

    # return render(request, 'users_app/sign_up2.html', {'form': form})
    return render(request, 'users_app/sign_up2.html')


# 문의

def user_inquire(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = InquireForm(request.POST)
            if form.is_valid():
                inquire = form.save(commit=False)
                inquire.user = request.user 
                inquire.inq_date = datetime.date.today()
                inquire.save()
                return redirect('user_mypage')
        else:
            form = InquireForm()
        return render(request, 'users_app/user_inquire.html', {'form': form})
    else:
        messages.warning(request, '먼저 로그인해주세요.')
        return redirect('sign_in')  # 로그인 페이지로 리디렉션    
    
    

# 마이페이지

# def user_mypage(request):
#     return render(request, 'users_app/user_mypage.html')

def camp_register(request):
    reg_requests = CampMemeberInfo.objects.filter(Q(id__id__contains=request.user.id))
    return render(request, 'users_app/user_mypage.html', {'reg_requests': reg_requests})

def camp_register_delete(request, camp_no):
    reg_requests = get_object_or_404(CampMemeberInfo, pk=camp_no)
    reg_requests.delete()
    return redirect('user_mypage')

# ajax

def user_booked_render(request):
    return render(request, 'users_app/user_booked.html')

def user_booked(request):
    template_name = 'users_app/user_booked.html'
    rendered_template = render(request, template_name)
    response_data = {
        'html': rendered_template.content.decode('utf-8')
    }

    return JsonResponse(response_data)


# book

def user_booked(request):
    print(request.user.id)
    bookings = Booking.objects.filter(Q(id__id__contains=request.user.id))
    # bookings = get_object_or_404(Booking, fk=user.id)
    # bookings = Booking.objects.get(id=request.user.id)
    return render(request, 'users_app/user_booked.html', {'bookings': bookings})

def user_booked_delete(request, book_no):
    bookings = get_object_or_404(Booking, pk=book_no)
    bookings.delete()
    return redirect('user_mypage')


# favorite

def user_favorite_list(request):
    print(request.user.id)
    favorites = FavoriteList.objects.filter(Q(id__id__contains=request.user.id))
    return render(request, 'users_app/user_favorite_list.html', {'favorites': favorites})

def user_favorite_delete(request, fav_id):
    Favorite = get_object_or_404(FavoriteList, pk=fav_id)
    Favorite.delete()
    return redirect('user_mypage')
    
    # review

def user_review_list(request):
    print(request.user.id)
    reviews = CampReview.objects.filter(Q(id__id__contains=request.user.id))
    return render(request, 'users_app/user_review_list.html', {'reviews': reviews})

def user_review_update(request, review_no):
    review = get_object_or_404(CampReview, pk=review_no)
    if request.method == "POST":
        form = campreviewform(request.POST, instance=review)
        if form.is_valid():
            form.save() 
            print("12312312")
            return redirect('user_mypage')   
        # messages.success(request, '수정되었습니다.')
 
    else:
        form = campreviewform(instance=review)
        # form = campreviewform(instance=review, 
        #                       initial={'camp_no': review.camp_no, 'id':review.id})
                            #   , 
                                    #    'rev_title':review.rev_title, 
                                    #    'rev_content':review.rev_content})
        print(form.errors)  # 유효성 검사 오류 메시지 출력
    return render(request, 'users_app/user_review_update.html', {'form':form})


def user_review_delete(request, review_no):
    review = get_object_or_404(CampReview, pk=review_no)
    review.delete()
    return redirect('user_mypage')



# inquiry


def user_inquiry_list(request):
    print(request.user.id)
    inquiries = UserInquire.objects.filter(Q(id__id__contains=request.user.id))
    return render(request, 'users_app/user_inquiry_list.html', {'inquiries': inquiries})


def user_inquiry_rep(request, inq_no):
    inquiry = get_object_or_404(UserInquire, inq_no=inq_no)
    reply = get_object_or_404(InqReply, inq_no=inq_no)

    return render(request, 'users_app/user_inquiry_rep.html', {'inquiry': inquiry, 'reply': reply})

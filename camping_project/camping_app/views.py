from tkinter import messagebox
from django.db.models import Q 
from django.shortcuts import render, get_object_or_404, redirect
from .models import CampInfo
from .forms import CampingForm
from django.views.generic import DetailView
from .models import ImageLink
from .models import CampFacInfo, CampReview
from .models import CampUtility
from .models import CampTypePrice, CampReview
from django.core.paginator import Paginator
import math
from .form_book import bookcampingForm
from .review_from import campreviewform


# Create your views here.
def index(request):
    camp_count = CampInfo.objects.count()
    return render(request, 'camping_app/index.html',{'camp_count':camp_count})

def camping_safety(request):
    return render(request, 'camping_app/camping_safety.html')


def camping_list(request):
    page = request.GET.get('page', 1)
    campings = Paginator(CampInfo.objects.all(), 10).get_page(page)

    # print(page)
    for camp in campings:
        camp.image_link = ImageLink.objects.get(camp_no=camp.camp_no)
        camp.camp_utility = CampUtility.objects.get(camp_no=camp.camp_no)

    start = math.floor((campings.number - 1) / 10) * 10 + 1
    end = min(campings.paginator.num_pages, start + 9)
    next_tens_page = math.ceil(campings.number / 10) * 10 + 1
    prev_tens_page = max(1, (math.floor((campings.number - 1) / 10) * 10))

    camp_count = CampInfo.objects.count()
    
    context = {
        'campings': campings,
        'page_range': range(start, end + 1),
        'next_tens_page': next_tens_page,
        'prev_tens_page': prev_tens_page,
        'camp_count':camp_count
    }

    return render(request, 'camping_app/camping_list.html', context)

def camping_new_list(request):
    page = request.GET.get('page', 1)
    campings = Paginator(CampInfo.objects.all().order_by('camp_no')[3371:], 10).get_page(page)

    # print(page)
    # for camp in campings:
        # camp.image_link = ImageLink.objects.get(camp_no=camp.camp_no)
        # camp.camp_utility = CampUtility.objects.get(camp_no=camp.camp_no)

    start = math.floor((campings.number - 1) / 10) * 10 + 1
    end = min(campings.paginator.num_pages, start + 9)
    next_tens_page = math.ceil(campings.number / 10) * 10 + 1
    prev_tens_page = max(1, (math.floor((campings.number - 1) / 10) * 10))

    camp_count = CampInfo.objects.all().order_by('camp_no')[3371:].count()
    
    context = {
        'campings': campings,
        'page_range': range(start, end + 1),
        'next_tens_page': next_tens_page,
        'prev_tens_page': prev_tens_page,
        'camp_count':camp_count
    }
    
    return render(request, 'camping_app/camping_new_list.html', context)

def camping_detail(request, camp_no):
    camping = get_object_or_404(CampInfo, pk=camp_no)
    tags = camping.camp_tag_li.split(',')
    tags = ['#' + tag for tag in tags if tag]
    image_links = get_object_or_404(ImageLink, pk=camp_no)
    camp_fac_info = get_object_or_404(CampFacInfo, pk=camp_no)
    camp_utility = get_object_or_404(CampUtility, pk=camp_no)
    reviews= CampReview.objects.filter(camp_no=camp_no)

    return render(request, 'camping_app/detail.html', {'camping': camping, 'image_links': image_links, 'camp_fac_info': camp_fac_info,'camp_utility':camp_utility,'tags':tags})


def camping_new_detail(request, camp_no):
    camping = get_object_or_404(CampInfo, pk=camp_no)
    tags = camping.camp_tag_li.split(',')
    tags = ['#' + tag for tag in tags if tag]
    reviews= CampReview.objects.filter(camp_no=camp_no)

    return render(request, 'camping_app/new_detail.html', {'camping': camping, 'tags':tags})

# def camping_insert(request):
#     if request.method == "POST":
#         form = CampingForm(request.POST)
#         if form.is_valid():
#             camping = form.save(commit=False)
#             camping.save()
#             return redirect('camping_list')
#     else:
#         form = CampingForm()

#     return render(request, 'camping_app/camping_form.html', {'form':form})

class CampImagesDetailView(DetailView):
    model = ImageLink
    template_name = 'detail.html'
    context_object_name = 'camp'

def camping_search_location(request):
    return render(request, 'camping_app/camping_search_location.html')

def camping_search(request, keyword=None, c_do=None, c_signgu=None, theme=None):
    # page = request.GET.get('page', 1)
    # print(page)
    
    # request.method == "POST" 조건을 삭제합니다.
    
    # if keyword:
    #     keyword = keyword.replace('-', ' ')
    
    keyword = request.GET.get('searchKrwd','') or keyword
    c_do = request.GET.get('c_do','') or c_do
    c_signgu = request.GET.get('c_signgu','') or c_signgu
    theme = request.GET.get('searchLctCl','') or theme
    
    # selected_seasons = (request.GET.get('camp_ope_period') or '').split(',')
    # selected_days = (request.GET.get('camp_ope_day') or '').split('+')
    # selected_types = (request.GET.get('camp_type') or '').split(',')
    # 필터링할 캠핑장 목록 초기화
    camp_list = CampInfo.objects.all()

    if keyword:
        # 키워드로 필터링
        camp_list = camp_list.filter(Q(camp_name__icontains=keyword) |
                                Q(camp_s_tt__icontains=keyword) |
                                Q(camp_itd__icontains=keyword))

    if c_do:
        # 지역 (c_do)로 필터링
        camp_list = camp_list.filter(Q(camp_address__icontains=c_do))

    if c_signgu:
        # 시/군 (c_signgu)로 필터링
        camp_list = camp_list.filter(Q(camp_address__icontains=c_signgu))

    if theme:
        # 테마 (theme)로 필터링
        camp_list = camp_list.filter(Q(camp_environment__icontains=theme))
    
    # if selected_seasons :
    #     for season in selected_seasons:
    #         camp_list = camp_list.filter(Q(camp_ope_period__icontains=season))
    
    # if selected_days :
    #     for day in selected_days:
    #         camp_list = camp_list.filter(Q(camp_ope_day__icontains=day))
    
    # if selected_types :
    #     for type in selected_types:
    #         camp_list = camp_list.filter(Q(camp_type__icontains=type))

    # 페이징
    paginator = Paginator(camp_list, 10)
    page = request.GET.get('page')
    campings = paginator.get_page(page)

    for camp in campings:
        camp.image_link = ImageLink.objects.get(camp_no=camp.camp_no)
        camp.camp_utility = CampUtility.objects.get(camp_no=camp.camp_no)

    start = math.floor((campings.number - 1) / 10) * 10 + 1
    end = min(campings.paginator.num_pages, start + 9)
    next_tens_page = math.ceil(campings.number / 10) * 10 + 1
    prev_tens_page = max(1, (math.floor((campings.number - 1) / 10) * 10))

    camp_count = camp_list.count()

    context = {
        'campings': campings,
        'page_range': range(start, end + 1),
        'next_tens_page': next_tens_page,
        'prev_tens_page': prev_tens_page,
        'camp_count': camp_count
    }


    return render(request, 'camping_app/camping_search_result.html',context)


    

def detail_intro(request, camp_no):
    image_links = get_object_or_404(ImageLink, pk=camp_no)
    camping = get_object_or_404(CampInfo, pk=camp_no)
    print(image_links)
    print(camping)
    return render(request, 'camping_app/detail_intro.html', {'image_links': image_links,'camping': camping})

def detail_text(request, camp_no):
    camp_type_price = get_object_or_404(CampTypePrice, pk=camp_no)
    print(camp_type_price)
    return render(request, 'camping_app/detail_text.html', {'camp_type_price': camp_type_price})

def detail_weather(request, camp_no):
    camping = get_object_or_404(CampInfo, pk=camp_no)
    print(camping)
    return render(request, 'camping_app/detail_weather.html', {'camping': camping})

def detail_map(request, camp_no):
    camping = get_object_or_404(CampInfo, pk=camp_no)
    print(camping)
    return render(request, 'camping_app/detail_map.html', {'camping': camping})

def detail_review(request, camp_no):
    # 필터링할 조건을 만들어 쿼리셋을 생성
    reviews = CampReview.objects.filter(camp_no=camp_no)
    
    # 필터링된 결과를 템플릿으로 전달
    return render(request, 'camping_app/detail_review.html', {'reviews': reviews})



# 캠핑 예약 - 로그인 시에만 가능 
def camping_book(request, camp_no):
    if request.user.is_authenticated:
        camping= get_object_or_404(CampInfo, pk=camp_no)
        # 1) 요청이 post 인지 확인하고 
        if request.method == "POST":
            #2) 폼 데이터의 내용을 form 변수에 저장
            forms = bookcampingForm(request.POST)
            #3) django 기본 기능인 is_valid() 사용해서 데이터 유효성 확인 
            if forms.is_valid():
                # 유효성 확인할 때 중복되면 오류창 뜸 
                # 4) form에 저장된 데이터를 아직 완전 저장하지 않고 
                # 현재는 이 부분 없어도 됨 : 저장 지연
                camping_book = forms.save(commit=False)
                # 수행할 작업이 있다면 여기서 수행 (우리는 현재 다른 작업 없음)
             
                # 5) 여기에서 db 저장 
                camping_book.save()
                # 6) db에 저장 후 결과 확인하기 위해 상품조회 화면으로 이동 (포워딩)
                # redirect() 사용
                return redirect('camping_list')
        else:
            forms = bookcampingForm(instance=camping)

        #7) else : post 요청이 아니라면 입력 폼 그대로 출력 
        return render(request, 'camping_app/camp_book.html', {'forms':forms})
    else:
        messagebox.showinfo('경고','로그인 후 가능합니다.')
        return redirect('../../../users/sign_in')
        # 비로그인 시 로그인 화면으로 이동 


# 리뷰 등록
def camping_review(request, camp_no):
    if request.user.is_authenticated:
        camping= get_object_or_404(CampInfo, pk=camp_no)
        # 1) 요청이 post 인지 확인하고 
        if request.method == "POST":
            #2) 폼 데이터의 내용을 form 변수에 저장
            rform = campreviewform(request.POST)
            #3) django 기본 기능인 is_valid() 사용해서 데이터 유효성 확인 
            if rform.is_valid():
                # 유효성 확인할 때 중복되면 오류창 뜸 
                # 4) form에 저장된 데이터를 아직 완전 저장하지 않고 
                # 현재는 이 부분 없어도 됨 : 저장 지연
                review_form = rform.save(commit=False)
                # 수행할 작업이 있다면 여기서 수행 (우리는 현재 다른 작업 없음)
         
                # 5) 여기에서 db 저장 
                review_form.save()
                # 6) db에 저장 후 결과 확인하기 위해 상품조회 화면으로 이동 (포워딩)
                # redirect() 사용
                return redirect('camping_list')
        else:
            rform = campreviewform(instance=camping)

        #7) else : post 요청이 아니라면 입력 폼 그대로 출력 
        return render(request, 'camping_app/camping_review.html', {'rform':rform})
    else:
        messagebox.showinfo('경고','로그인 후 가능합니다.')
        return redirect('../../../users/sign_in')
        # 비로그인 시 로그인 화면으로 이동 

def camping_secondhanded(request):
    return render(request, 'camping_app/camping_secondhanded.html')

def camping_insert(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CampingForm(request.POST)
            if form.is_valid():
                camping = form.save(commit=False)
                camping.save()
                return redirect('camping_list')
        else:
            form = CampingForm()

        return render(request, 'camping_app/camping_form.html', {'form':form})
    else:
        messagebox.showinfo('경고','로그인 후 가능합니다.')
        return redirect('../../../users/sign_in')
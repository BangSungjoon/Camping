from django.db.models import Q 
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
import os
from .models import CampInfo
from .forms import CampingForm
from django.views.generic import DetailView
from .models import ImageLink
from .models import CampFacInfo
from .models import CampUtility
from django.core.paginator import Paginator
import math

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
    
def camping_detail(request, camp_no):
    camping = get_object_or_404(CampInfo, pk=camp_no)
    tags = camping.camp_tag_li.split(',')
    tags = ['#' + tag for tag in tags if tag]
    image_links = get_object_or_404(ImageLink, pk=camp_no)
    camp_fac_info = get_object_or_404(CampFacInfo, pk=camp_no)
    camp_utility = get_object_or_404(CampUtility, pk=camp_no)

    return render(request, 'camping_app/detail.html', {'camping': camping, 'image_links': image_links, 'camp_fac_info': camp_fac_info,'camp_utility':camp_utility,'tags':tags})


def camping_insert(request):
    if request.method == "POST":
        form = CampingForm(request.POST)
        if form.is_valid():
            camping = form.save(commit=False)
            camping.save()
            return redirect('camping_list')
    else:
        form = CampingForm()

    return render(request, 'camping_app/camping_form.html', {'form':form})

class CampImagesDetailView(DetailView):
    model = ImageLink
    template_name = 'detail.html'
    context_object_name = 'camp'

# def detail(request):
#     return render(request, 'camping_app/detail.html')

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

def get_detail_intro(request):
    try:
        with open(os.path.join(os.path.dirname(__file__), 'camping_app/detail_intro.html'), 'r') as file:
            content = file.read()
        # HTML 형식으로 반환
        return HttpResponse(content, content_type='text/html')
    except Exception as e:
        # 오류 발생 시 JSON 형식으로 반환
        return JsonResponse({'error': 'Failed to load content'})

def detail_intro3(request, camp_no):
    try:
        with open(os.path.join(os.path.dirname(__file__), f'camping_app/detail_intro.html'), 'r') as file:
            content = file.read()
        # HTML 형식으로 반환
        return HttpResponse(content, content_type='text/html')
    except Exception as e:
        # 오류 발생 시 처리
        return HttpResponse('Failed to load content', status=404)
    
def detail_intro(request):
    return render(request, 'camping_app/detail_intro.html')
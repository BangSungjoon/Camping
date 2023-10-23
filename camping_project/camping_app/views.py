from tkinter import messagebox
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
import os
from .models import CampInfo
from .forms import CampingForm
from django.views.generic import DetailView
from .models import ImageLink
from .models import CampFacInfo
from .models import CampUtility
from .form_book import bookcampingForm

# Create your views here.
def index(request):
    return render(request, 'camping_app/index.html')

def camping_safety(request):
    return render(request, 'camping_app/camping_safety.html')

# def camping_list(request):
#     return render(request, 'camping_app/camping_list.html')

# def camping_detail(request):
#     return render(request, 'camping_app/camping_detail.html')

def camping_list(request):
    campings = CampInfo.objects.all()
    return render(request, 'camping_app/camping_list.html', {'campings':campings})

def camping_detail(request, camp_no):
    camping = get_object_or_404(CampInfo, pk=camp_no)
    image_links = get_object_or_404(ImageLink, pk=camp_no)
    camp_fac_info = get_object_or_404(CampFacInfo, pk=camp_no)
    camp_utility = get_object_or_404(CampUtility, pk=camp_no)

    return render(request, 'camping_app/detail.html', {'camping': camping, 'image_links': image_links, 'camp_fac_info': camp_fac_info,'camp_utility':camp_utility})


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


# 캠핑 예약 - 로그인 시에만 가능 
def camping_book(request, camp_no):
    # if request.user.is_authenticated:
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
                product_book = forms.save(commit=False)
                # 수행할 작업이 있다면 여기서 수행 (우리는 현재 다른 작업 없음)
                # product.....() 작업 
                # 5) 여기에서 db 저장 
                product_book.save()
                # 6) db에 저장 후 결과 확인하기 위해 상품조회 화면으로 이동 (포워딩)
                # redirect() 사용
                return redirect('product_list')
        else:
            forms = bookcampingForm(instance=camping)

        #7) else : post 요청이 아니라면 입력 폼 그대로 출력 
        return render(request, 'camping_app/camp_book.html', {'forms':forms})
    # else:
    #     messagebox.showinfo('경고','로그인 후 가능합니다.')
    #     return redirect('../../../users/sign_in')
    #     # 비로그인 시 로그인 화면으로 이동 
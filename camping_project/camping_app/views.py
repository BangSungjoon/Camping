from django.shortcuts import render, get_object_or_404, redirect
from .models import CampInfo
from .forms import CampingForm
from django.views.generic import DetailView
from .models import ImageLink
from .models import CampFacInfo
from .models import CampUtility

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

# def detail_intro(request):
#     return render(request, 'camping_app/detail_intro.html')

# def detail_intro(request):
#     # 데이터베이스에서 이미지 링크를 조회하거나 원하는 방식으로 데이터를 가져옴
#     image_links = ImageLink.objects.all()  # 예시로 모든 이미지 링크를 가져옴

#     context = {
#         'image_links': image_links  # 템플릿으로 전달할 데이터를 context에 추가
#     }

#     return render(request, 'camping_app/detail_intro.html', context)

# def detail_intro(request, camp_no):
#     # 데이터베이스에서 camp_no와 일치하는 데이터를 조회
#     try:
#         image_links = ImageLink.objects.get(camp_no=camp_no)
#     except ImageLink.DoesNotExist:
#         # 예외 처리: 해당 camp_no를 가진 데이터가 없는 경우
#         image_links = None

#     context = {
#         'image_links': image_links
#     }

#     return render(request, 'camping_app/detail_intro.html', context)

def detail_intro(request, camp_no):
    image_links = get_object_or_404(ImageLink, pk=camp_no)
    print(image_links)
    return render(request, 'camping_app/detail_intro.html', {'image_links': image_links})

def detail_text(request, camp_no):
    camping = get_object_or_404(CampInfo, pk=camp_no)
    print(camping)
    return render(request, 'camping_app/detail_text.html', {'camping': camping})
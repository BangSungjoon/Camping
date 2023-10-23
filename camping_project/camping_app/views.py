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

def detail_intro(request, camp_no):
    image_links = get_object_or_404(ImageLink, pk=camp_no)
    print(image_links)
    return render(request, 'camping_app/detail_intro.html', {'image_links': image_links})

def detail_text(request, camp_no):
    camping = get_object_or_404(CampInfo, pk=camp_no)
    print(camping)
    return render(request, 'camping_app/detail_text.html', {'camping': camping})

def detail_weather(request):
    return render(request, 'camping_app/detail_weather.html')

def detail_map(request):
    return render(request, 'camping_app/detail_map.html')
from django.shortcuts import render, get_object_or_404, redirect
from .models import CampInfo
from .forms import CampingForm
from django.views.generic import DetailView
from .models import ImageLink


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
    return render(request, 'camping_app/camping_detail.html', {'camping':camping})

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
    template_name = 'camping_detail.html'
    context_object_name = 'camp'
    
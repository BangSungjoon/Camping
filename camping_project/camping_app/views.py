from django.shortcuts import render
from django.http import JsonResponse
from .models import CampingSite

def index(request):
    return render(request, 'camping_app/index.html')

# 검색창 열기
def camping_search_form(request):
    return render(request, 'camping_app/search_camping_sites.html')

def search_camping_sites(request):
    query = request.GET.get('query', '')
    results = CampingSite.objects.filter(name__icontains=query)
    data = [{'name': site.name, 'location': site.location, 'description': site.description} for site in results]
    return JsonResponse(data, safe=False)
from django.shortcuts import render

def index(request):
    return render(request, 'camping_app/index.html')

def detail(request):
    return render(request, 'camping_app/detail.html')
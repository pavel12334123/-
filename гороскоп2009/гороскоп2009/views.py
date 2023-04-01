from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return HttpResponse('<h1>главная</h1>')

def index(request):
    return render(request, 'index.html')
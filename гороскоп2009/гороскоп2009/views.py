from django.http import HttpResponse
from django.shortcuts import render
from .models import Sign


def homepage(request):
    return HttpResponse('<h1>главная</h1>')


def index(request):
    return render(request, 'index.html')


def sign(request, name, to, end):
    try:
        new_sign = Sign(name=name, to_date=to, from_date=end)
        new_sign.save()
        return HttpResponse(f"<h3>id: {new_sign.id} name: {new_sign.name}</h3>")
    except Exception as k:
        return HttpResponse(f"<h1><b>{k}</b></h1>")

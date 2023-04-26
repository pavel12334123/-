from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('about/', views.index),
    path('sign/<name>/<to>/<end>', views.sign),
    path('signs', views.Sign)
]

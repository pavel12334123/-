from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.index),
    path('sign/<name>/<to>/<end>', views.Sign),
    path('signs', views.Sign),
    path('predict/<sign>', views.predict)
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.index),
    path('sign/<name>/<to>/<end>', views.sign),
    path('product/add', views.add_product),
    path('signs', views.sign),
    path('predict/<sign>', views.predict)
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.index),
    path('sign/<name>/<to>/<end>', views.sign),
    path('product/add', views.add_predict),
    path('signs', views.sign),
    path('predit/<param_sign>', views.predict)
]

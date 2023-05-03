from django.http import HttpResponse
from django.shortcuts import render
from .models import Sign
from .forms import ProductName
from .models import Product


def homepage(request):
    return HttpResponse('<h1>главная</h1>')


def index(request):
    return render(request, 'index.html')


def Sign(request, name, to, end):
    try:
        new_sign = Sign(name=name, to_date=to, from_date=end)
        new_sign.save()
        return HttpResponse(f"<h3>id: {new_sign.id} name: {new_sign.name}</h3>")
    except Exception as k:
        return HttpResponse(f"<h1><b>{k}</b></h1>")


def product_new(request):
    if request.method == "POST":
        try:
            if request.method == "POST":
                form = ProductName(request.POST)
                if form.is_valid():
                    name = form['product_name'].value()
                    product = Product(name=name)
                    product.save()
                    return HttpResponse(f"<h3>id: {product.id} name: {product.name}</h3>")
        except Exception as e:
            return HttpResponse(f"<h1><b>يباسينبتاسنيتبتسبتيستمتسيتنبمتنبنمنتشبلتنيسبتمن</b>{e}</h1>")
    else:
        form = ProductName()
        return render(request, "addProduct.html", {'form': form})


def predict(req, sign_name):
    predict_list=[]
    for predict in Predict.objects.all():
        if predict.Sign.name == sign_name:
            predict_list.append(predict)
    return render(req, "", {})


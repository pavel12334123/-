from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Sign
from .forms import ProductName
from .models import Product, Predection, Sign


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


def predict(req, sign):
    # predict_list=[]
    # for predict in Predection.objects.all():
    #     if predict.Sign.id == sign:
    #         predict_list.append(predict)
    signs = Sign.objects.all()
    predict_list = [
        Predection(sign=_sign, text="ABOBA") for _sign in signs
    ]
    out = []
    for pre in predict_list:
        if pre.sign.id == int(sign):
            out.append(pre)
    return render(req, "prediction.html", {'pre':out})

def add_product(request):
    if request.method == "POST":
        try:
            form = ProductName(request.POST)
            if form.is_valid():
                name = form['product_name'].value()
                predection = Predection(text=name)
                predection.save()
                return redirect("/")
        except Exception as e:
            form = ProductName(request.POST)
            return render(request, "addProduct.html", {
                'form': form,
                'error_message': e
            })
    else:
        form = ProductName()
        return render(request, "addProduct.html", {'form': form})

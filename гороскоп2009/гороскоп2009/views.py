import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Sign
from .forms import PredictName
from .models import Predict, Predection, Sign


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


def predict(req, param_sign: int):
    predict_list=[]
    for PREDICT in Predection.objects.all():
        if PREDICT.sign.id == int(param_sign):
            predict_list.append(PREDICT)

    return render(req, "prediction.html", {'pre':predict_list})



def add_predict(request):
    if request.method == "POST":
        try:
            form = PredictName(request.POST)
            if form.is_valid():
                sign_id = form["sign"].value()
                name = form['predict_name'].value()
                predection = Predection(text=name, sign=Sign.objects.get(id=sign_id))
                predection.date = datetime.date.today()
                predection.save()
                return redirect("/")
        except Exception as e:
            form = PredictName(request.POST)
            return render(request, "addProduct.html", {
                'form': form,
                'error_message': e
            })
    else:
        form = PredictName()
        return render(request, "addProduct.html", {'form': form})

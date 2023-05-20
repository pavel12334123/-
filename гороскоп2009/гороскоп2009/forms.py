from django import forms
from .models import Sign


class PredictName(forms.Form):
    predict_name = forms.CharField(label="Создай гороскоп", max_length=200)
    sign = forms.ModelChoiceField(widget=forms.Select,
                                      queryset=Sign.objects.all())
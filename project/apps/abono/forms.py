from django import forms

from .models import Abono


class AbonoForm(forms.ModelForm):
    class Meta:
        model = Abono
        fields = ["producto", "cantidad"]
        widgets = {
            "producto": forms.Select(attrs={"class": "form-control"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control"}),
        }

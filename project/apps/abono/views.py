from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models


class AbonoDetail(DetailView):
    model = models.Abono


class AbonoList(ListView):
    model = models.Abono

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Abono.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Abono.objects.all()
        return object_list


class AbonoCreate(CreateView):
    model = models.Abono
    form_class = forms.AbonoForm
    success_url = reverse_lazy("venta:index")

    def form_valid(self, form):
        form.instance.abonado = self.request.user.abonado  # type: ignore
        return super().form_valid(form)


class AbonoDelete(DeleteView):
    model = models.Abono
    success_url = reverse_lazy("abono:abono_list")


class AbonoUpdate(UpdateView):
    model = models.Abono
    success_url = reverse_lazy("abono:abono_list")
    form_class = forms.AbonoForm

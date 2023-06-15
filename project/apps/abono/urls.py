from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="abono/index.html"), name="index"),
    path("abono/list/", views.AbonoList.as_view(), name="abono_list"),
    path("abono/detail/<int:pk>", views.AbonoDetail.as_view(), name="abono_detail"),
    path("abono/create/", staff_member_required(views.AbonoCreate.as_view()), name="venta_create"),
    path("abono/delete/<int:pk>", staff_member_required(views.AbonoDelete.as_view()), name="abono_delete"),
    path("abono/update/<int:pk>", staff_member_required(views.AbonoUpdate.as_view()), name="abono_update"),
]

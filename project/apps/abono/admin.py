from django.contrib import admin

from . import models

admin.site.register(models.Abonado)


@admin.register(models.Abono)
class AbonoAdmin(admin.ModelAdmin):
    list_display = (
        "abonado",
        "producto",
        "cantidad",
        "precio_total",
        "fecha_abono",
    )
    list_display_links = ("producto",)
    search_fields = ("producto.nombre", "abonado")
    list_filter = ("abonado",)
    date_hierarchy = "fecha_abono"

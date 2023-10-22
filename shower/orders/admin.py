from django.contrib import admin
from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["campaign", "amount", "currency", "status", "invoice_id"]


@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    ...

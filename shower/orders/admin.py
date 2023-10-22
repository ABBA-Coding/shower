from django.contrib import admin
from django.utils.timesince import timesince

from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["campaign", "amount", "currency", "status", "display_created_at", "invoice_id"]

    def display_created_at(self, obj):
        return timesince(obj.created_at) + ' ago'

    display_created_at.short_description = 'Updated at'

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    list_display = ["amount", "currency", "is_deleted"]

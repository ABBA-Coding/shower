from django.contrib import admin

from shower.businesses.models import Business, Sites


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    ...


@admin.register(Sites)
class SitesAdmin(admin.ModelAdmin):
    ...

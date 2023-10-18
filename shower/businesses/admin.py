from django.contrib import admin

from shower.businesses.models import Business, Category


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

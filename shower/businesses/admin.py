from django.contrib import admin

from shower.businesses.models import Business, Sites, Category


class SitesInline(admin.TabularInline):
    model = Sites
    extra = 1


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    inlines = [SitesInline]


@admin.register(Sites)
class SitesAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

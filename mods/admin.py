from django.contrib import admin

from mods.models import Mod, Category


@admin.register(Mod)
class ModAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'created', 'is_published')
    list_display_linkes = ('id', 'name')
    ordering = ['created', 'name']


@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_linkes = ('id', 'title')



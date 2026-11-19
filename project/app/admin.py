from django.contrib import admin
from .models import Bosh_sahifa, Boglanish, Sotuvchilar


@admin.register(Bosh_sahifa)
class Bosh_sahifaAdmin(admin.ModelAdmin):
    search_fields=('kompyuter_nomi',)
    list_filter=('kompyuter_nomi',)

@admin.register(Boglanish)
class BoglanishAdmin(admin.ModelAdmin):
    search_fields = ('adminni_ismi',)
    list_filter = ('adminni_ismi',)


@admin.register(Sotuvchilar)
class SotuvchilarAdmin(admin.ModelAdmin):
    search_fields=('sotuvchilar_ismi',)
    list_filter=('sotuvchilar_ismi',)












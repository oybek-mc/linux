from django.shortcuts import render
from .models import Bosh_sahifa, Boglanish, Sotuvchilar


def bosh_sahifa(request):
    kompyuterlar = Bosh_sahifa.objects.all()
    return render(request, 'bosh_sahifa.html', {
        'kompyuterlar': kompyuterlar,
    })


def boglanish(request):
    adminlar = Boglanish.objects.all()
    return render(request, 'boglanish.html', {
        'adminlar': adminlar,
    })


def sotuvchilar(request):
    sotuvchilar_royxati = Sotuvchilar.objects.all()
    return render(request, 'sotuvchilar.html', {
        'sotuvchilar': sotuvchilar_royxati,
    })
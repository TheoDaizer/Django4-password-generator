from django.shortcuts import render
from django.http import HttpResponse
from string import ascii_lowercase, ascii_uppercase, digits
from random import choice

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list(ascii_lowercase)
    if request.GET.get('uppercase'):
        characters.extend(ascii_uppercase)
    if request.GET.get('digits'):
        characters.extend(digits)
    if request.GET.get('symbols'):
        characters.extend('!@#$%^&*()')

    length = int(request.GET.get('length', 12))
    res = ''.join(choice(characters) for _ in range(length))

    return render(request, 'generator/password.html', {'password': res})


def about(request):
    return render(request, 'generator/about.html')
# from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Comando para execultar: py .\manage.py runserver
# Abrir no navegador: localhost:8000

# Create your views here.

# def home(request):
#      return render(request, 'home.html')

def home(request):
    return render(request,'recipes/pages/home.html', context={'name': 'Jonatas Pedro'})


def detalhes(request):
    return render(request,'recipes/pages/detalhes.html', context={'name': 'Jonatas Pedro'})

# def home(request):
#     return render(request,'recipes/pages/home.html')

# def home(request):
#     return render(request,'recipes/pages/search.html')


# def index(request):
#     return HttpResponse('home.html')


def sobre(request):
    return HttpResponse('<h1>SOBRE - Django</h1>')

def contato(request):
    return HttpResponse('<h1>CONTATO - Django</h1>')
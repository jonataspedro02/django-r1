from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
# HTTP RESPONSE

def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Jonatas Pedro'})

def sobre(request):
    return render(request,'sobre.html')

def contatos(request):
  return render(request, 'recipes/pages/contatos.html', context={'name': 'Jonatas Pedro'})

def receitas(request):
    return render(request, 'recipes/pages/receitas.html', context={'name': 'Jonatas Pedro'})
# Create your views here.

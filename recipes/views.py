from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
# HTTP RESPONSE

def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Shelbys'})

def sobre(request):
    return render(request,'sobre.html')

def contatos(request):
  return render(request, 'recipes/pages/contatos.html', context={'name': 'Shelbys'})

def contatos_2(request):
  return render(request, 'recipes/pages/contatos_2.html', context={'name': 'Shelbys'})

def contatos_3(request):
  return render(request, 'recipes/pages/contatos_3.html', context={'name': 'Shelbys'})
def receitas(request):
    return render(request, 'recipes/pages/receitas.html', context={'name': 'Shelbys'})

def receitas_2(request):
    return render(request, 'recipes/pages/receitas_2.html', context={'name': 'Shelbys'})

def receitas_3(request):
    return render(request, 'recipes/pages/receitas_3.html', context={'name': 'Shelbys'})

# Create your views here.

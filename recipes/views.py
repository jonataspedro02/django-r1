from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def home(request):
    return render(request,'recipes/pages/home.html', context={'name': 'Jonatas Pedro'})

def receita(request):
    return render(request,'recipes/portials/receita.html', context={'name': 'Jonatas Pedro'})

   
# def receita(request):
#     return HttpResponseRedirect('recipes/portials/receita.html')

def sobre(request):
    return HttpResponse('SOBRE - hello django')

def contato(request):
    return HttpResponse('CONTATO - hello django')
# Create your views here.

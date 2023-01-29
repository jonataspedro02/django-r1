from django.urls import path
from recipes.views import home, sobre, contatos, contatos_2, contatos_3, receitas, receitas_2, receitas_3

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contatos/', contatos, name='contatos'),
    path('contatos_2/', contatos_2, name='contatos_2'),
    path('contatos_3/', contatos_3, name='contatos_3'),
    path('receitas/', receitas, name='receitas'),
    path('receitas_2/', receitas_2, name='receitas_2'),
    path('receitas_3/', receitas_3, name='receitas_3')
]
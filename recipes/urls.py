from django.urls import path
from recipes.views import home, sobre, contatos, receitas

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contatos/', contatos, name='contatos'),
    path('receita/', receitas, name='receitas')
]
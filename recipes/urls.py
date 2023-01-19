# from django.contrib import admin
from django.urls import path
from recipes.views import home, detalhes

urlpatterns = [
    # path('admin/', admin.site.urls),
     path('', home),
    path('detalhes/', detalhes, name='detalhes'),
]
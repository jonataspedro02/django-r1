# from django.contrib import admin
from django.urls import path
from recipes.views import home, novo

urlpatterns = [
    # path('admin/', admin.site.urls),
     path('', home),
    path('novo/', novo, name='novo'),
]
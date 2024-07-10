from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls ),
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('login/', views.login, name='login'),
]

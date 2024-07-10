from django.contrib import admin
from django.urls import path, include
from austral.views import *
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('vehiculos/', views.vehiculos, name='vehiculos'),
]
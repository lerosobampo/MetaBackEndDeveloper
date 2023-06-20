# URLS.PY APP LEVEL

from django.contrib import admin
from django.urls import path
#from .views import sayHello
#from .views import index
from . import views

urlpatterns = [
    #path('', sayHello, name='sayHello'),
    path('', views.index, name='index'),
]
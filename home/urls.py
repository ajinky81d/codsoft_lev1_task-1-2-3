

from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("portfolio",views.portfolio,name='portfolio'),
    path("calculator",views.calculator,name='calculator'),
    path("contact",views.index,name='contact')
     
]

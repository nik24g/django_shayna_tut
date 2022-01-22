from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about),
    path('contact/', views.contact, name='contact')
]

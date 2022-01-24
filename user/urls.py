from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about),
    path('contact/', views.contact, name='contact'),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('signup', views.signup, name='signup')
]

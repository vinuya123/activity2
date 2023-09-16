from django.contrib import admin
from django.urls import path, include
from portfolio import views

urlpatterns = [
    path('', views.portfolio, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects'),
]
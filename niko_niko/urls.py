from django.urls import path
from . import views

app_name = 'niko_niko'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('about/', views.about, name='about'),
    path('faqs/', views.faqs, name='faqs'),
]
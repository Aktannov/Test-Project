from django.urls import path, include
from .views import dataview



urlpatterns = [
    path('', dataview, name='menu'),
    path('<str:menu>/', dataview, name='menu'),
]

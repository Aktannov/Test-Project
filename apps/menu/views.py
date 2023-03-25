from django.shortcuts import render
from .models import (
    Menu,
)


def dataview(request, menu=None):
    if menu:
        current_menu = Menu.objects.get(name=menu)
    else:
        current_menu = None
    
    context = {
        'menu': current_menu.children.all() if current_menu else Menu.objects.all()
    }
    return render(request, 'info/index.html', context)
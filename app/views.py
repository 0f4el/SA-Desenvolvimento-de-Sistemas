
from django.shortcuts import render

def login_view (request):
    """Exibe a tela de login"""
    return render(request, 'login.html')

def homepage_view (request):
    """Exibe a homepage"""
    return render(request, 'homepage.html')

def cadastro_view (request):
    """Exibe a tela de cadastro"""
    return render(request, 'cadastro.html')

def em_desenvolvimento_view (request):
    """Exibe uma tela placeholder"""
    return render(request, 'placeholder.html')
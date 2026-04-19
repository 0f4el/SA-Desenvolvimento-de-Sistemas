
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.homepage_view, name='homepage'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('placeholder/', views.em_desenvolvimento_view, name='placeholder')
]
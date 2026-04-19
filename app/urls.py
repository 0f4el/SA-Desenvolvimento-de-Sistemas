
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
"""
    OBSERVAÇÃO: FAZER COM QUE O PLACEHOLDER SO POSSA SER ACESSADO SE FIZER LOGIN
"""



urlpatterns = [
    #URLs sem login
    path('placeholder/', views.em_desenvolvimento_view, name='placeholder'),
    path('', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),

    # URLs que precisam de login
    path('home/', views.homepage_view, name='homepage'),
    
    # Logout (redireciona para login)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
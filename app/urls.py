
from django.urls import include, path
from . import views
from .api_views import NotebookViewSet, RackViewSet, SalaViewSet
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"salas", SalaViewSet, basename="api-salas")
router.register(r"racks", RackViewSet, basename="api-racks")
router.register(r"notebooks", NotebookViewSet, basename="api-notebooks")


urlpatterns = [
    # API
    path('api/', include(router.urls)),

    #URLs sem login
    path('placeholder/', views.em_desenvolvimento_view, name='placeholder'),
    path('', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),

    # URLs que precisam de login
    path('home/', views.homepage_view, name='homepage'),
    path('salas/nova/', views.sala_create_view, name='sala_create'),
    path('salas/<int:sala_id>/editar/', views.sala_update_view, name='sala_update'),
    path('salas/<int:sala_id>/excluir/', views.sala_delete_view, name='sala_delete'),
    path('salas/<int:sala_id>/racks/novo/', views.rack_create_view, name='rack_create'),
    path('salas/<int:sala_id>/racks/', views.racks_da_sala_view, name='racks_da_sala'),
    path('racks/<int:rack_id>/editar/', views.rack_update_view, name='rack_update'),
    path('racks/<int:rack_id>/excluir/', views.rack_delete_view, name='rack_delete'),
    path('racks/<int:rack_id>/notebooks/novo/', views.notebook_create_view, name='notebook_create'),
    path('racks/<int:rack_id>/notebooks/', views.notebooks_do_rack_view, name='notebooks_do_rack'),
    path('notebooks/<int:notebook_id>/editar/', views.notebook_update_view, name='notebook_update'),
    path('notebooks/<int:notebook_id>/excluir/', views.notebook_delete_view, name='notebook_delete'),
    
    # Logout (redireciona para login)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]

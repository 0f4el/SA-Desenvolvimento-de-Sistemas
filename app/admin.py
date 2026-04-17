from django.contrib import admin
from .models import Cadastro

@admin.register(Cadastro)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email', 'instituicao', 'cargo')  # Campos exibidos na lista
    search_fields = ('nome','id', 'cpf', 'email')


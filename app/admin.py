from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cadastro, Notebook, Rack, Sala

@admin.register(Cadastro)
class CadastroAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'cpf', 'instituicao', 'cargo')
    list_filter = ('cargo', 'instituicao')
    search_fields = ('username', 'email', 'cpf')
    
    # Oculta superusuários da lista
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_superuser=False)
    
    fieldsets = (
        ('Dados Pessoais', {'fields': ('username', 'email', 'password', 'cpf')}),
        ('Dados Institucionais', {'fields': ('instituicao', 'cargo')}),
        ('Permissões', {'fields': ('is_active',)}),  # ← só is_active, sem staff e superuser
    )
    
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2', 'cpf', 'instituicao', 'cargo'),
        }),
    )

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ("nome", "bloco", "numero", "andar")
    search_fields = ("nome", "bloco", "numero")


@admin.register(Rack)
class RackAdmin(admin.ModelAdmin):
    list_display = ("identificador", "sala", "status", "quantidade_slots", "temperatura")
    list_filter = ("status", "sala")
    search_fields = ("identificador", "sala__nome", "sala__numero")


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = ("tag", "modelo", "rack", "numero_slot", "status", "ultima_atualizacao")
    list_filter = ("status", "rack", "rack__sala")
    search_fields = ("tag", "modelo", "rack__identificador", "rack__sala__nome")

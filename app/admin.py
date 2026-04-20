from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cadastro

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
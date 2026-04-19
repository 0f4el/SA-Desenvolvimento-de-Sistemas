from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cadastro

"""
    OBSERVAÇÂO: Revisar as permissões na url admin de algum usuario
    Porque esta aparecendo isso dai:

Permissões

Active
Designates whether this user should be treated as active. Unselect this instead of deleting accounts.

Staff status
Designates whether the user can log into this admin site.

Superuser status
Designates that this user has all permissions without explicitly assigning them.
Delete

"""


@admin.register(Cadastro)
class CadastroAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'cpf', 'instituicao', 'cargo')
    search_fields = ('username', 'email', 'cpf')
    
    # Oculta superusuários da lista
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_superuser=False)
    
    fieldsets = (
        ('Dados Pessoais', {'fields': ('username', 'email', 'password', 'cpf')}),
        ('Dados Institucionais', {'fields': ('instituicao', 'cargo')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2', 'cpf', 'instituicao', 'cargo'),
        }),
    )
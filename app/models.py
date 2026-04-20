from django.db import models
from django.contrib.auth.models import AbstractUser

#Cadastro
class Cadastro(AbstractUser):
    """
    Herda do AbstractUser que já tem: username, password, first_name, last_name, email
    """
    nome = models.CharField('Nome Completo', max_length=60)
    cpf = models.CharField(unique=True, max_length=11, editable=True)
    instituicao = models.CharField('Instituição', max_length=200)
    
    class Cargo(models.TextChoices):
        PROFESSOR = 'professor', 'Professor'
        TUTOR = 'tutor', 'Tutor'
        GESTOR = 'gestor', 'Gestor'
        ALUNO = 'aluno', 'Aluno'

    cargo = models.CharField('Cargo',max_length=20,choices=Cargo.choices,help_text='Selecione o cargo')

    # #SALVAR SENHA COMO HASH - DAR UMA OLHADA
    #     def salvar_com_hash(self):
    #     """Salva a senha com hash (mais seguro)"""
    #     if self.senha and not self.senha.startswith('pbkdf2_'):
    #         self.senha = make_password(self.senha)
    #     self.save()
    #⚠️ Importante: Isso funciona mas a senha está sendo salva em texto puro no banco, o que não é seguro. Quando quiser melhorar, use o sistema de autenticação do Django (django.contrib.auth) que faz hash da senha automaticamente. Quer implementar isso agora ou deixa pra depois?

    # #VERIFICAR SENHA
    # def verificar_senha(self, senha_plain):
    #     """Verifica se a senha está correta"""
    #     return check_password(senha_plain, self.senha)

    class Meta:
        verbose_name = 'Cadastro'
        verbose_name_plural = 'Cadastros'

    
    def __str__(self):
        return f"{self.username} - {self.get_cargo_display()}"
    
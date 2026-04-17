from django.db import models

#Cadastro
class Cadastro(models.Model):
    nome = models.CharField('Nome Completo', max_length=60)
    cpf = models.CharField(unique=True, max_length=11, editable=True)
    email = models.EmailField('E-mail', unique=True)
    senha = models.CharField('Senha', max_length=100, blank=False, null=False)
    instituicao = models.CharField('Instituição', max_length=200)
    class Cargo(models.TextChoices):
        PROFESSOR = 'professor', 'Professor'
        TUTOR = 'tutor', 'Tutor'
        GESTOR = 'gestor', 'Gestor'
        ALUNO = 'aluno', 'Aluno'

    cargo = models.CharField('Cargo',max_length=20,choices=Cargo.choices,default=Cargo.ALUNO,help_text='Selecione o cargo')

    # #SALVAR SENHA COMO HASH - DAR UMA OLHADA
    #     def salvar_com_hash(self):
    #     """Salva a senha com hash (mais seguro)"""
    #     if self.senha and not self.senha.startswith('pbkdf2_'):
    #         self.senha = make_password(self.senha)
    #     self.save()

    # #VERIFICAR SENHA
    # def verificar_senha(self, senha_plain):
    #     """Verifica se a senha está correta"""
    #     return check_password(senha_plain, self.senha)

    class Meta:
        verbose_name = 'Cadastro'
        verbose_name_plural = 'Cadastros'

    
    def __str__(self):
        return f"{self.nome} - {self.get_cargo_display()}"
    

#Login

#Dashboard
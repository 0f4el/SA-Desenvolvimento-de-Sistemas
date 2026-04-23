from django.db import models
from django.contrib.auth.models import AbstractUser


class Cadastro(AbstractUser):
    """
    Herda do AbstractUser que já tem: username, password, first_name, last_name, email
    """
    nome = models.CharField('Nome Completo', max_length=60)
    cpf = models.CharField(
        unique=True,
        max_length=11,
        editable=True,
        error_messages={"unique": "Já existe um cadastro com este CPF."},
    )
    instituicao = models.CharField('Instituição', max_length=200)
    
    class Cargo(models.TextChoices):
        PROFESSOR = 'professor', 'Professor'
        TUTOR = 'tutor', 'Tutor'
        GESTOR = 'gestor', 'Gestor'
        ALUNO = 'aluno', 'Aluno'

    cargo = models.CharField(
        'Cargo (professor, tutor, gestor ou aluno)',
        max_length=20,
        choices=Cargo.choices,
        help_text='Selecione o cargo'
    )
    REQUIRED_FIELDS = ["email", "cpf", "instituicao", "cargo"]

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

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    bloco = models.CharField(max_length=50, blank=True)
    numero = models.CharField(max_length=20)
    andar = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} ({self.numero})"

class Rack(models.Model):
    class Status(models.TextChoices):
        ATIVO = "ativo", "Ativo"
        MANUTENCAO = "manutencao", "Manutenção"
        INATIVO = "inativo", "Inativo"

    identificador = models.CharField(
        max_length=50,
        unique=True,
        error_messages={"unique": "Já existe um rack com este identificador."},
    )
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name="racks")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ATIVO)
    quantidade_slots = models.PositiveIntegerField(default=10)
    temperatura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "Rack"
        verbose_name_plural = "Racks"
        ordering = ["identificador"]

    def __str__(self):
        return f"Rack {self.identificador} - {self.sala.nome}"

class Notebook(models.Model):
    class Status(models.TextChoices):
        DISPONIVEL = "disponivel", "Disponível"
        EM_USO = "em_uso", "Em uso"
        MANUTENCAO = "manutencao", "Manutenção"
        AUSENTE = "ausente", "Ausente"

    tag = models.CharField(
        max_length=50,
        unique=True,
        error_messages={"unique": "Já existe um notebook com esta tag."},
    )
    modelo = models.CharField(max_length=100)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE, related_name="notebooks")
    numero_slot = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DISPONIVEL)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Notebook"
        verbose_name_plural = "Notebooks"
        ordering = ["rack", "numero_slot"]
        constraints = [
            models.UniqueConstraint(
                fields=["rack", "numero_slot"],
                name="unique_slot_por_rack",
                violation_error_message="Já existe um notebook cadastrado neste slot para este rack.",
            )
        ]

    def __str__(self):
        return f"{self.tag} - Slot {self.numero_slot} ({self.rack.identificador})"

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import Cadastro


def login_view(request):
    """Exibe a tela de login usando a autenticação Django"""

    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('password')
        
        try:
            usuario = Cadastro.objects.get(email=email)
            username = usuario.username
        except Cadastro.DoesNotExist:
            username = None
        
        if username:
            user = authenticate(request, username=username, password=senha)
        else:
            user = None
        
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'E-mail ou senha inválidos')

    return render(request, 'login.html')


@login_required
def homepage_view(request):
    """Homepage protegida"""
    return render(request, 'homepage.html', {
        'usuario': request.user
    })


def logout_view(request):
    """Faz logout"""
    logout(request)
    return redirect('login')


def cadastro_view(request):
    """Exibe a tela de cadastro"""
    if request.method == 'POST':
        nome = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        cpf = request.POST.get('cpf')
        instituicao = request.POST.get('instituicao')
        cargo = request.POST.get('cargo')
        


        """
        ESSA PARTE ESTA BUGANDO
        BUGS: As mensagens de erro não estão desaparecendo depois de corrigir o camopo, e ela não some quando aparece a mensagem "Por favor, preencha todos os campos.";
        O campo que está errado não fica contornado de vermelho;
        Aparentemente o cargo pode não estar salvando no model(ou então o model que nao esta mostrando certo no admin)       
        """
        # Verifica se nome já existe
        if Cadastro.objects.filter(username=nome).exists():
            messages.error(request, 'Este nome de usuário já está em uso!')
            return render(request, 'cadastro.html')

        # Verifica se email já existe
        if Cadastro.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado!')
            return render(request, 'cadastro.html')
        
        # Verifica se CPF já existe
        if Cadastro.objects.filter(cpf=cpf).exists():
            messages.error(request, 'Este CPF já está cadastrado!')
            return render(request, 'cadastro.html')
        """
        ESSA PARTE ESTA BUGANDO  
        """
        
        # Cria o usuário
        Cadastro.objects.create(
            username=nome,
            email=email,
            password=make_password(senha),
            cpf=cpf,
            instituicao=instituicao,
            cargo=cargo
        )
        
        return redirect('login')

    return render(request, 'cadastro.html')


def em_desenvolvimento_view(request):
    """Exibe uma tela placeholder"""
    return render(request, 'placeholder.html')
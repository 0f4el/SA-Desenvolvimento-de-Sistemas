from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from .forms import NotebookForm, RackForm, SalaForm
from .models import Cadastro, Notebook, Rack, Sala


def login_view(request):
    """Exibe a tela de login usando a autenticação Django"""
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('password')
        
        try:
            #busca no banco quem tem esse email para descobrir o username
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
        
        erros = {}

        # Verifica se nome já existe
        if Cadastro.objects.filter(username=nome).exists():
            erros['username'] = 'Este nome de usuário já está em uso!'
        # Verifica se email já existe
        if Cadastro.objects.filter(email=email).exists():
            erros['email'] = 'Este e-mail já está cadastrado!'
        # Verifica se CPF já existe
        if Cadastro.objects.filter(cpf=cpf).exists():
            erros['cpf'] = 'Este CPF já está cadastrado!'
        if erros:
            return render(request, 'cadastro.html', {'erros': erros, 'dados': request.POST})

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

@login_required
def homepage_view(request):
    """Homepage protegida"""
    salas = Sala.objects.all()
    return render(request, 'homepage.html', {
        'usuario': request.user,
        'salas': salas,
    })


@login_required
def sala_create_view(request):
    form = SalaForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Sala cadastrada com sucesso.")
            return redirect("homepage")
        messages.error(request, "Nao foi possivel cadastrar a sala. Verifique os campos.")

    return render(request, "sala_form.html", {
        "usuario": request.user,
        "form": form,
        "titulo": "Cadastrar sala",
        "texto_botao": "Salvar sala",
    })


@login_required
def sala_update_view(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    form = SalaForm(request.POST or None, instance=sala)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Sala atualizada com sucesso.")
            return redirect("homepage")
        messages.error(request, "Nao foi possivel atualizar a sala. Verifique os campos.")

    return render(request, "sala_form.html", {
        "usuario": request.user,
        "form": form,
        "sala": sala,
        "titulo": "Editar sala",
        "texto_botao": "Salvar alterações",
    })


@login_required
def sala_delete_view(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)

    if request.method == "POST":
        sala.delete()
        messages.success(request, "Sala excluida com sucesso.")
        return redirect("homepage")

    return render(request, "sala_confirm_delete.html", {
        "usuario": request.user,
        "sala": sala,
    })


@login_required
def rack_create_view(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    form = RackForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            rack = form.save(commit=False)
            rack.sala = sala
            rack.save()
            messages.success(request, "Rack cadastrado com sucesso.")
            return redirect("racks_da_sala", sala_id=sala.id)
        messages.error(request, "Nao foi possivel cadastrar o rack. Verifique os campos.")

    return render(request, "rack_form.html", {
        "usuario": request.user,
        "form": form,
        "sala": sala,
        "titulo": "Cadastrar rack",
        "texto_botao": "Salvar rack",
    })


@login_required
def rack_update_view(request, rack_id):
    rack = get_object_or_404(Rack, id=rack_id)
    form = RackForm(request.POST or None, instance=rack)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Rack atualizado com sucesso.")
            return redirect("racks_da_sala", sala_id=rack.sala.id)
        messages.error(request, "Nao foi possivel atualizar o rack. Verifique os campos.")

    return render(request, "rack_form.html", {
        "usuario": request.user,
        "form": form,
        "sala": rack.sala,
        "rack": rack,
        "titulo": "Editar rack",
        "texto_botao": "Salvar alterações",
    })


@login_required
def rack_delete_view(request, rack_id):
    rack = get_object_or_404(Rack.objects.select_related("sala"), id=rack_id)

    if request.method == "POST":
        sala_id = rack.sala.id
        rack.delete()
        messages.success(request, "Rack excluido com sucesso.")
        return redirect("racks_da_sala", sala_id=sala_id)

    return render(request, "rack_confirm_delete.html", {
        "usuario": request.user,
        "rack": rack,
        "sala": rack.sala,
    })


@login_required
def racks_da_sala_view(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    racks = Rack.objects.filter(sala=sala).prefetch_related('notebooks').order_by('identificador')

    for rack in racks:
        notebooks_por_slot = {notebook.numero_slot: notebook for notebook in rack.notebooks.all()}
        slot_indicators = []

        for numero_slot in range(1, rack.quantidade_slots + 1):
            notebook = notebooks_por_slot.get(numero_slot)
            if notebook is None:
                slot_indicators.append({
                    'numero_slot': numero_slot,
                    'status_class': 'vazio',
                    'descricao': f'Slot {numero_slot} vazio',
                })
                continue

            slot_indicators.append({
                'numero_slot': numero_slot,
                'status_class': notebook.status.replace('_', '-'),
                'descricao': f"Slot {numero_slot}: {notebook.tag} - {notebook.get_status_display()}",
            })

        rack.slot_indicators = slot_indicators
        rack.slots_ocupados = len(notebooks_por_slot)

    return render(request, 'racks.html', {
        'usuario': request.user,
        'sala': sala,
        'racks': racks,
    })


@login_required
def notebooks_do_rack_view(request, rack_id):
    rack = get_object_or_404(Rack.objects.select_related('sala').prefetch_related('notebooks'), id=rack_id)
    notebooks_por_slot = {notebook.numero_slot: notebook for notebook in rack.notebooks.all()}
    slot_items = []

    for numero_slot in range(1, rack.quantidade_slots + 1):
        notebook = notebooks_por_slot.get(numero_slot)
        if notebook is None:
            slot_items.append({
                'numero_slot': numero_slot,
                'status': 'vazio',
                'status_label': 'Vazio',
                'tag': None,
                'modelo': None,
                'ultima_atualizacao': None,
                'tem_notebook': False,
            })
            continue

        slot_items.append({
            'numero_slot': numero_slot,
            'status': notebook.status,
            'status_label': notebook.get_status_display(),
            'notebook_id': notebook.id,
            'tag': notebook.tag,
            'modelo': notebook.modelo,
            'ultima_atualizacao': notebook.ultima_atualizacao,
            'tem_notebook': True,
        })

    return render(request, 'notebooks.html', {
        'usuario': request.user,
        'rack': rack,
        'sala': rack.sala,
        'slot_items': slot_items,
        'slots_ocupados': len(notebooks_por_slot),
    })


@login_required
def notebook_create_view(request, rack_id):
    rack = get_object_or_404(Rack.objects.select_related("sala"), id=rack_id)
    initial = {}
    slot_inicial = request.GET.get("slot")
    if slot_inicial and slot_inicial.isdigit():
        initial["numero_slot"] = int(slot_inicial)

    form = NotebookForm(request.POST or None, initial=initial)

    if request.method == "POST":
        if form.is_valid():
            notebook = form.save(commit=False)
            notebook.rack = rack
            if notebook.numero_slot > rack.quantidade_slots:
                form.add_error("numero_slot", f"O rack possui apenas {rack.quantidade_slots} slots.")
                messages.error(request, "Nao foi possivel cadastrar o notebook. Verifique os campos.")
                return render(request, "notebook_form.html", {
                    "usuario": request.user,
                    "form": form,
                    "rack": rack,
                    "sala": rack.sala,
                    "titulo": "Cadastrar notebook",
                    "texto_botao": "Salvar notebook",
                })
            try:
                notebook.full_clean()
                notebook.save()
                messages.success(request, "Notebook cadastrado com sucesso.")
                return redirect("notebooks_do_rack", rack_id=rack.id)
            except ValidationError as exc:
                for errors in exc.message_dict.values():
                    for error in errors:
                        form.add_error(None, error)
        messages.error(request, "Nao foi possivel cadastrar o notebook. Verifique os campos.")

    return render(request, "notebook_form.html", {
        "usuario": request.user,
        "form": form,
        "rack": rack,
        "sala": rack.sala,
        "titulo": "Cadastrar notebook",
        "texto_botao": "Salvar notebook",
    })


@login_required
def notebook_update_view(request, notebook_id):
    notebook = get_object_or_404(Notebook.objects.select_related("rack", "rack__sala"), id=notebook_id)
    form = NotebookForm(request.POST or None, instance=notebook)

    if request.method == "POST":
        if form.is_valid():
            notebook_atualizado = form.save(commit=False)
            notebook_atualizado.rack = notebook.rack
            if notebook_atualizado.numero_slot > notebook.rack.quantidade_slots:
                form.add_error("numero_slot", f"O rack possui apenas {notebook.rack.quantidade_slots} slots.")
                messages.error(request, "Nao foi possivel atualizar o notebook. Verifique os campos.")
                return render(request, "notebook_form.html", {
                    "usuario": request.user,
                    "form": form,
                    "rack": notebook.rack,
                    "sala": notebook.rack.sala,
                    "notebook": notebook,
                    "titulo": "Editar notebook",
                    "texto_botao": "Salvar alterações",
                })
            try:
                notebook_atualizado.full_clean()
                notebook_atualizado.save()
                messages.success(request, "Notebook atualizado com sucesso.")
                return redirect("notebooks_do_rack", rack_id=notebook.rack.id)
            except ValidationError as exc:
                for errors in exc.message_dict.values():
                    for error in errors:
                        form.add_error(None, error)
        messages.error(request, "Nao foi possivel atualizar o notebook. Verifique os campos.")

    return render(request, "notebook_form.html", {
        "usuario": request.user,
        "form": form,
        "rack": notebook.rack,
        "sala": notebook.rack.sala,
        "notebook": notebook,
        "titulo": "Editar notebook",
        "texto_botao": "Salvar alterações",
    })


@login_required
def notebook_delete_view(request, notebook_id):
    notebook = get_object_or_404(Notebook.objects.select_related("rack", "rack__sala"), id=notebook_id)

    if request.method == "POST":
        rack_id = notebook.rack.id
        notebook.delete()
        messages.success(request, "Notebook excluido com sucesso.")
        return redirect("notebooks_do_rack", rack_id=rack_id)

    return render(request, "notebook_confirm_delete.html", {
        "usuario": request.user,
        "notebook": notebook,
        "rack": notebook.rack,
        "sala": notebook.rack.sala,
    })

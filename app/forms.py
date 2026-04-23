from django import forms

from .models import Notebook, Rack, Sala


class BaseCrudForm(forms.ModelForm):
    default_error_messages = {
        "required": "Este campo é obrigatório.",
        "invalid": "Informe um valor válido.",
        "unique": "Já existe um registro com este valor.",
        "max_value": "Informe um valor menor ou igual ao permitido.",
        "min_value": "Informe um valor maior ou igual ao permitido.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            for error_key, message in self.default_error_messages.items():
                field.error_messages[error_key] = message


class SalaForm(BaseCrudForm):
    class Meta:
        model = Sala
        fields = ["nome", "bloco", "numero", "andar"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "bloco": forms.TextInput(attrs={"class": "form-control"}),
            "numero": forms.TextInput(attrs={"class": "form-control"}),
            "andar": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_nome(self):
        return self.cleaned_data["nome"].strip()

    def clean_bloco(self):
        return self.cleaned_data["bloco"].strip()

    def clean_numero(self):
        return self.cleaned_data["numero"].strip()

    def clean_andar(self):
        return self.cleaned_data["andar"].strip()


class RackForm(BaseCrudForm):
    class Meta:
        model = Rack
        fields = ["identificador", "status", "quantidade_slots", "temperatura"]
        widgets = {
            "identificador": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "quantidade_slots": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "temperatura": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }

    def clean_identificador(self):
        return self.cleaned_data["identificador"].strip()


class NotebookForm(BaseCrudForm):
    class Meta:
        model = Notebook
        fields = ["tag", "modelo", "numero_slot", "status"]
        widgets = {
            "tag": forms.TextInput(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "numero_slot": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }

    def clean_tag(self):
        return self.cleaned_data["tag"].strip()

    def clean_modelo(self):
        return self.cleaned_data["modelo"].strip()

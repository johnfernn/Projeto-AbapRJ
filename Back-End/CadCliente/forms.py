# forms.py
from django import forms
from .models import Cadastro, MembroFamilia


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = "__all__"


class CadastroFamily(forms.ModelForm):
    class Meta:
        model = MembroFamilia
        fields = "__all__"

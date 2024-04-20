from django.contrib import admin
from .models import Cadastro, MembroFamilia


@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    ...


@admin.register(MembroFamilia)
class MembroFamiliaAdmin(admin.ModelAdmin):
    ...


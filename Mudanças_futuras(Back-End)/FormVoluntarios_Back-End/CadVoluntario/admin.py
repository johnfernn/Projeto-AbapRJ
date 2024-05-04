from django.contrib import admin
from .models import CadastroVoluntario


@admin.register(CadastroVoluntario)
class CadastroVoluntarioAdmin(admin.ModelAdmin):
    ...




from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CadastroVoluntario(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True, default='Sem nome', unique=True, verbose_name='Nome', help_text='Digite o nome aqui.')
    email = models.EmailField(verbose_name='E-mail', max_length=255, unique=True)
    senha = models.CharField(max_length=100)
    confirmar_senha = models.CharField(max_length=100)

    def clean(self):
        if self.senha != self.confirmar_senha:
            raise ValidationError("As senhas não coincidem.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    telefone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Telefone')
    cpf = models.CharField(max_length=14, null=True, blank=True, verbose_name='CPF')
    descricao = models.TextField(null=True, blank=True, verbose_name='Descrição')
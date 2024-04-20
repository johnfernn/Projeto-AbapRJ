from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Cadastro(models.Model):
    nome = models.CharField(max_length=100, null=True)
    cpf = models.CharField(max_length=11, null=True)
    data_de_nascimento = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def idade(self):
        if self.data_de_nascimento:
            hoje = date.today()
            idade = hoje.year - self.data_de_nascimento.year
            return idade
        else:
            return None


class MembroFamilia(models.Model):
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE, related_name='membrosFamilia')
    nome = models.CharField(max_length=100)
    SEXO_CHOICES = (
        ('feminino', 'Feminino'),
        ('masculino', 'Masculino'),
        ('outros', 'Outros'),
    )
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)

    def __str__(self):
        return self.cadastro.nome

    is_published = models.BooleanField(default=True)


"""
 local_nascimento = models.CharField(max_length=100)
 bairro = models.CharField(max_length=100)
 cidade = models.CharField(max_length=100)
 estado = models.CharField(max_length=100)
 endereco = models.CharField(max_length=255)
 cep = models.CharField(max_length=20)
 complemento = models.CharField(max_length=100)
 celular = models.CharField(max_length=20)
 telefone = models.CharField(max_length=20)
 parentesco = models.CharField(max_length=100)
 grau_instrucao = models.CharField(max_length=100)
 religiao = models.CharField(max_length=100)
 atividade = models.CharField(max_length=100)
 gosta_fazer = models.CharField(max_length=255)
 data_primeiro_contato = models.DateField()
 sexo = models.CharField(max_length=10)
 estado_civil = models.CharField(max_length=20)
 cpf = models.CharField(max_length=20)
 rg = models.CharField(max_length=20)
 profissao = models.CharField(max_length=100)
 escolaridade = models.CharField(max_length=100)
 ocupacao_atual = models.CharField(max_length=100)
 beneficios_governamentais = models.TextField()
 forma_renda = models.CharField(max_length=100)
 valor = models.DecimalField(max_digits=10, decimal_places=2)

 rua = models.CharField(max_length=100)
 comodos = models.IntegerField()
 propriedade = models.CharField(max_length=20)
 tipo_moradia = models.CharField(max_length=20)
 plano_saude = models.CharField(max_length=10)
 aposentadoria = models.CharField(max_length=10, )
 beneficios = models.CharField(max_length=255)
 bens_consumo = models.CharField(max_length=255)
 num_pessoas = models.IntegerField()
 renda_familiar = models.CharField(max_length=100)
 estruturas_rua_bairro = models.CharField(max_length=255)
 situacao_familiar = models.CharField(max_length=100)
 is_published = models.BooleanField(default=False)
"""

"""
   data_nascimento = models.DateField()
   estado_civil = models.CharField(max_length=20)
   vinculo_familiar = models.CharField(max_length=100)
   telefone = models.CharField(max_length=20, blank=True, null=True)
   celular = models.CharField(max_length=20)
   rg = models.CharField(max_length=20)
   cpf = models.CharField(max_length=20)
   escolaridade = models.CharField(max_length=100)
   profissao = models.CharField(max_length=100)
   renda = models.DecimalField(max_digits=10, decimal_places=2)
   ocupacao_atual = models.CharField(max_length=100)
   is_published = models.BooleanField(default=False)
"""

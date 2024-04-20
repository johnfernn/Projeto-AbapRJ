from django.db import models
from django.db import models


class DadosCrianca(models.Model):
    tipos_beneficio_Gov = (
        ("Fed", "Federais"),
        ("Est", "Estaduais"),
        ("Mun", "Municipais"),
        ("BF", "Bolsa Familia"),
        ("BPC", "Benefício de Prestação Continuada"),
        ("PETI", "Programa de Erradicação do Trabalho Infantil"),
        ("O", "Outros"),
    )
    sexo_tipo = (("M", "Masculino"), ("F", "Feminino"))
    nome = models.CharField(max_length=100, null=False)
    endereco = models.CharField(max_length=300)  # endereço e numero
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100, null=True)
    celular = models.CharField(max_length=100)  # default='+00 (00) 00000-0000'
    sexo = models.CharField(max_length=100, choices=sexo_tipo)
    data_nascimento = models.DateField(null=True)
    estado_civil = models.CharField(max_length=100, null=True)
    rg = models.CharField(max_length=100, null=False)
    DExp = models.DateField(null=True)
    cpf = models.CharField(max_length=14, default="000.000.000-00")
    escolaridade = models.CharField(max_length=100, null=True)
    profissao = models.CharField(max_length=100, null=True)
    renda = models.FloatField(null=True)
    ocupacao_atual = models.CharField(max_length=100, null=True)
    beneficio_Gov = models.CharField(
        max_length=4, null=True, choices=tipos_beneficio_Gov
    )
    renda_Gov = models.FloatField(null=True)

    criar_tabela_membros = models.BooleanField(default=False)

    tipo_moradia = (
        ("A", "Aluguel"),
        ("C", "Cessão"),
        ("F", "Financiada"),
        ("I", "Invasão"),
        ("P", "Própria"),
    )
    tipo_morada = (
        ("Alvenida", "Alvenida"),
        ("Papelão", "Papelão"),
        ("Palafita", "Palafita"),
        ("Madeira", "Madeira"),
        ("Lona", "Lona"),
        ("Plástico", "Plástico"),
    )
    minha_moradia = models.CharField(max_length=1, choices=tipo_moradia, null=True)
    minha_morada = models.CharField(max_length=10, choices=tipo_morada, null=True)
    quantidade_comodos = models.IntegerField(null=True)
    quartos = models.IntegerField(null=True)
    sala = models.IntegerField(null=True)
    cozinhas = models.IntegerField(null=True)
    banheiros = models.IntegerField(null=True)
    agua_encanada = models.BooleanField(default=False)
    esgoto = models.BooleanField(default=False)
    energia = models.BooleanField(default=False)
    coleta_lixo = models.BooleanField(default=False)


class MembroFamilia(models.Model):
    sexo_tipo = (("M", "Masculino"), ("F", "Feminino"))
    familia = models.ForeignKey(DadosCrianca, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, null=False)
    sexo = models.CharField(max_length=100, choices=sexo_tipo)
    data_nascimento = models.DateField(null=True)
    estado_civil = models.CharField(max_length=100, null=True)
    vinculo_familia = models.CharField(max_length=100, null=True)
    telefone = models.CharField(max_length=100, null=True)
    celular = models.CharField(max_length=100)  # default='+00 (00) 00000-0000'
    escolaridade = models.CharField(max_length=100, null=True)
    profissao = models.CharField(max_length=100, null=True)
    renda = models.FloatField(null=True)
    ocupacao_atual = models.CharField(max_length=100, null=True)

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DadosCrianca",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("endereco", models.CharField(max_length=300)),
                ("bairro", models.CharField(max_length=100)),
                ("cep", models.CharField(max_length=100)),
                ("complemento", models.CharField(max_length=100)),
                ("cidade", models.CharField(max_length=100)),
                ("estado", models.CharField(max_length=100)),
                ("telefone", models.CharField(max_length=100, null=True)),
                ("celular", models.CharField(max_length=100)),
                (
                    "sexo",
                    models.CharField(
                        choices=[("M", "Masculino"), ("F", "Feminino")], max_length=100
                    ),
                ),
                ("data_nascimento", models.DateField(null=True)),
                ("estado_civil", models.CharField(max_length=100, null=True)),
                ("rg", models.CharField(max_length=100)),
                ("DExp", models.DateField(null=True)),
                ("cpf", models.CharField(default="000.000.000-00", max_length=14)),
                ("escolaridade", models.CharField(max_length=100, null=True)),
                ("profissao", models.CharField(max_length=100, null=True)),
                ("renda", models.FloatField(null=True)),
                ("ocupacao_atual", models.CharField(max_length=100, null=True)),
                (
                    "beneficio_Gov",
                    models.CharField(
                        choices=[
                            ("Fed", "Federais"),
                            ("Est", "Estaduais"),
                            ("Mun", "Municipais"),
                            ("BF", "Bolsa Familia"),
                            ("BPC", "Benefício de Prestação Continuada"),
                            ("PETI", "Programa de Erradicação do Trabalho Infantil"),
                            ("O", "Outros"),
                        ],
                        max_length=4,
                        null=True,
                    ),
                ),
                ("renda_Gov", models.FloatField(null=True)),
                ("criar_tabela_membros", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="MembroFamilia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                (
                    "sexo",
                    models.CharField(
                        choices=[("M", "Masculino"), ("F", "Feminino")], max_length=100
                    ),
                ),
                ("data_nascimento", models.DateField(null=True)),
                ("estado_civil", models.CharField(max_length=100, null=True)),
                ("vinculo_familia", models.CharField(max_length=100, null=True)),
                ("telefone", models.CharField(max_length=100, null=True)),
                ("celular", models.CharField(max_length=100)),
                ("escolaridade", models.CharField(max_length=100, null=True)),
                ("profissao", models.CharField(max_length=100, null=True)),
                ("renda", models.FloatField(null=True)),
                ("ocupacao_atual", models.CharField(max_length=100, null=True)),
                (
                    "familia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cadastra_kid.dadoscrianca",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Moradia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "minha_moradia",
                    models.CharField(
                        choices=[
                            ("A", "Aluguel"),
                            ("C", "Cessão"),
                            ("F", "Financiada"),
                            ("I", "Invasão"),
                            ("P", "Própria"),
                        ],
                        max_length=1,
                    ),
                ),
                (
                    "minha_morada",
                    models.CharField(
                        choices=[
                            ("Alvenida", "Alvenida"),
                            ("Papelão", "Papelão"),
                            ("Palafita", "Palafita"),
                            ("Madeira", "Madeira"),
                            ("Lona", "Lona"),
                            ("Plástico", "Plástico"),
                        ],
                        max_length=10,
                    ),
                ),
                ("quantidade_comodos", models.IntegerField()),
                ("quartos", models.IntegerField()),
                ("sala", models.IntegerField()),
                ("cozinhas", models.IntegerField()),
                ("banheiros", models.IntegerField()),
                ("agua_encanada", models.BooleanField()),
                ("esgoto", models.BooleanField()),
                ("energia", models.BooleanField()),
                ("coleta_lixo", models.BooleanField()),
                (
                    "familia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cadastra_kid.dadoscrianca",
                    ),
                ),
            ],
        ),
    ]

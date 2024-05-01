from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastra_kid", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="dadoscrianca",
            name="agua_encanada",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="dadoscrianca",
            name="banheiros",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="dadoscrianca",
            name="coleta_lixo",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="dadoscrianca",
            name="cozinhas",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="dadoscrianca",
            name="energia",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="dadoscrianca",
            name="esgoto",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="dadoscrianca",
            name="minha_morada",
            field=models.CharField(
                choices=[
                    ("Alvenida", "Alvenida"),
                    ("Papelão", "Papelão"),
                    ("Palafita", "Palafita"),
                    ("Madeira", "Madeira"),
                    ("Lona", "Lona"),
                    ("Plástico", "Plástico"),
                ],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="dadoscrianca",
            name="minha_moradia",
            field=models.CharField(
                choices=[
                    ("A", "Aluguel"),
                    ("C", "Cessão"),
                    ("F", "Financiada"),
                    ("I", "Invasão"),
                    ("P", "Própria"),
                ],
                max_length=1,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="dadoscrianca",
            name="quantidade_comodos",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="dadoscrianca",
            name="quartos",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="dadoscrianca",
            name="sala",
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name="Moradia",
        ),
    ]

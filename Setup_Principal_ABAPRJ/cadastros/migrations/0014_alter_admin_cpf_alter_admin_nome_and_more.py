# Generated by Django 5.0.6 on 2024-05-15 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0013_alter_admin_cpf_alter_admin_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='cpf',
            field=models.CharField(blank=True, help_text='Digite seu CPF aqui. ', max_length=14, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='nome',
            field=models.CharField(help_text='Digite o nome aqui.', max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='cadastrovoluntario',
            name='cpf',
            field=models.CharField(blank=True, help_text='Digite seu CPF aqui modelo: 000.000.000-00 ', max_length=14, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='cadastrovoluntario',
            name='email',
            field=models.EmailField(error_messages={'blank': 'Este campo não pode ficar em branco.', 'invalid': 'O valor fornecido é inválido, verifique se tem @.'}, help_text='Digite o E-mail aqui.', max_length=255, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='cadastrovoluntario',
            name='nome',
            field=models.CharField(help_text='Digite o nome aqui.', max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='cadastrovoluntario',
            name='telefone',
            field=models.CharField(blank=True, help_text='Digite seu Telefone aqui. como no exemplo: (21) 90000-0000', max_length=15, verbose_name='Telefone'),
        ),
        migrations.DeleteModel(
            name='Atualizar',
        ),
    ]

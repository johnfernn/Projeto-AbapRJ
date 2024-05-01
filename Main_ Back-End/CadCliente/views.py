from django.shortcuts import render, redirect
from .models import Cadastro, MembroFamilia
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


def register_view(request):
    if request.method == 'POST':
        data = request.POST.get('data_de_nascimento')
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')

        # instância de Cadastro
        cad = Cadastro.objects.create(
            data_de_nascimento=data,
            nome=nome,
            cpf=cpf
        )

        nome2 = request.POST.getlist('nome2')
        sexo = request.POST.getlist('sexo')

        for nome_membro, sexo_membro in zip(nome2, sexo):
            MembroFamilia.objects.create(
                nome=nome_membro,
                sexo=sexo_membro,
                cadastro=cad
            )

        return HttpResponseRedirect(reverse_lazy('home'))

    return render(request, 'dados/cadCliente.html')

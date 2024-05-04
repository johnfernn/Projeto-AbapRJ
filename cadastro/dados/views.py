from django.db.models import Q
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView
from CadCliente.models import Cadastro


class Home(ListView):
    model = Cadastro
    template_name = 'dados/home.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Cadastro.objects.filter(is_published=True, ).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Home'
        return context


class Procurar(ListView):
    model = Cadastro
    template_name = 'dados/procurar.html'
    success_url = reverse_lazy('procurar')

    def get_queryset(self):
        procurar_termo = self.request.GET.get('q', '').strip()
        if not procurar_termo:
            raise Http404()

        return Cadastro.objects.filter(
            Q(Q(nome__icontains=procurar_termo) | Q(cpf__icontains=procurar_termo), ), is_published=True, ).order_by(
            "-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        procurar_termo = self.request.GET.get('q', '').strip()
        context['page_title'] = f'Procurar por "{procurar_termo}" |',
        context['procurar_termo'] = procurar_termo,
        return context


class DadosCadastros(ListView):
    model = Cadastro
    template_name = 'dados/dadosCadastro.html'

    def get_queryset(self):
        dados_id = self.kwargs.get('dados_id')
        return Cadastro.objects.filter(id=dados_id, is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalhes do Cadastro'
        return context

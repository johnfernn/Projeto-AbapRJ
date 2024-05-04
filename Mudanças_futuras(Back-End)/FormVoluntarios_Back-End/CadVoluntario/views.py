from django.db.models import Q
from django.http import Http404
from django.urls import reverse_lazy
from .models import CadastroVoluntario
from django.views.generic import ListView, CreateView


class Home(ListView):
    model = CadastroVoluntario
    template_name = 'CadVoluntario/home.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return CadastroVoluntario.objects.filter().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Home'
        return context


class Procurar(ListView):
    model = CadastroVoluntario
    template_name = 'CadVoluntario/procurar.html'
    success_url = reverse_lazy('procurar')

    def get_queryset(self):
        procurar_termo = self.request.GET.get('q', '').strip()
        if not procurar_termo:
            raise Http404()

        return CadastroVoluntario.objects.filter(
            Q(Q(nome__icontains=procurar_termo) | Q(cpf__icontains=procurar_termo), )).order_by(
            "-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        procurar_termo = self.request.GET.get('q', '').strip()
        context['page_title'] = f'Procurar por "{procurar_termo}" |',
        context['procurar_termo'] = procurar_termo,
        return context


class DadosCadastros(ListView):
    model = CadastroVoluntario
    template_name = 'CadVoluntario/dadosCadastro.html'

    def get_queryset(self):
        dados_id = self.kwargs.get('dados_id')
        return CadastroVoluntario.objects.filter(id=dados_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalhes do Cadastro'
        return context


class CadCreateView(CreateView):
    model = CadastroVoluntario
    fields = "__all__"
    success_url = reverse_lazy("home")

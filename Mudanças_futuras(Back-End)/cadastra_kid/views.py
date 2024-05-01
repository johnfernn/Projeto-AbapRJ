from datetime import date

from django.shortcuts import (
    get_object_or_404,
)  # atalho para fazer a busca de um determinado item!!! //Estudart shortcusts do Jg
from django.urls import (
    reverse_lazy,
)  # pega o nome da rota e ele retorna a rota completa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

from .models import DadosCrianca


class TodoListView(ListView):
    model = DadosCrianca


class TodoCreateView(CreateView):
    model = DadosCrianca
    fields = "__all__"
    success_url = reverse_lazy("cad_list")


class TodoUpdateView(UpdateView):
    model = DadosCrianca
    fields = "__all__"
    success_url = reverse_lazy("cad_list")


class TodoDeleteView(DeleteView):
    model = DadosCrianca
    success_url = reverse_lazy("cad_list")


class TodoCompleteView(View):
    pass
    # def get(self, request, pk):
    #     todo = get_object_or_404(DadosCrianca, pk=pk)
    #     todo.dataEntrega = date.today()
    #     todo.save()
    #     return reverse_lazy("cad_list")

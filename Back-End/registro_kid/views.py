from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

from django.shortcuts import get_object_or_404
from django.urls import (reverse_lazy)

from .models import DadosCrianca
# from datetime import date


class CadListView(ListView):
    model = DadosCrianca


class CadCreateView(CreateView):
    model = DadosCrianca
    fields = "__all__"

    success_url = reverse_lazy("cad_list")


class CadUpdateView(UpdateView):
    model = DadosCrianca
    fields = "__all__"

    success_url = reverse_lazy("cad_list")


class CadDeleteView(DeleteView):
    model = DadosCrianca
    success_url = reverse_lazy("cad_list")

#
# class TodoCompleteView(View):
#     def get(self, request, pk):
#         todo = get_object_or_404(DadosCrianca, pk=pk)
#         todo.dataEntrega = date.today()
#         todo.save()
#
#     success_url = reverse_lazy("todo_list")

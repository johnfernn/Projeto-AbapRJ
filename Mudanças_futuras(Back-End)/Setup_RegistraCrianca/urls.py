from django.contrib import admin
from django.urls import path

from cadastra_kid.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="cad_list"),
    path("create", TodoCreateView.as_view(), name="cad_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="cad_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="cad_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="cad_complete"),
]

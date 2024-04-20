from django.contrib import admin
from django.urls import path
from registro_kid.views import (
    CadListView,
    CadCreateView,
    CadUpdateView,
    CadDeleteView,

)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CadListView.as_view(), name='cad_list'),
    path("create", CadCreateView.as_view(), name="cad_create"),
    path("update/<int:pk>", CadUpdateView.as_view(), name="cad_update"),
    path("delete/<int:pk>", CadDeleteView.as_view(), name="cad_delete"),
]

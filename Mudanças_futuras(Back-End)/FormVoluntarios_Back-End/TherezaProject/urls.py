from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from CadVoluntario.views import Home, Procurar, DadosCadastros, CadCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("create", CadCreateView.as_view(), name="funcionarioForm"),
    path("cadastro/procurar/", Procurar.as_view(), name="procurar"),
    path("cadastro/CadVoluntario/<int:dados_id>/", DadosCadastros.as_view(), name="dadosCadastros"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)








from django.conf.urls import include, url
from django.contrib import admin

from core.views import Index, IndexDetail, Cadastro, CadastroOrigem,CadastroDestino

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^cadastro/$', Cadastro.as_view(), name='cadastro'),
    url(r'cadastro/origem/$', CadastroOrigem.as_view(), name="origem"),
    url(r'cadastro/destino/$', CadastroDestino.as_view(), name="destino"),
    url(r'^(?P<slug>[-\w]+)/$', IndexDetail.as_view(), name='index-detail'),
]

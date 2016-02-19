from django.conf.urls import include, url
from django.contrib import admin

from core.views import Index, IndexDetail, Cadastro

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$', IndexDetail.as_view(), name='index-detail'),
    url(r'^cadastro/$', Cadastro.as_view(), name='cadastro'),
]

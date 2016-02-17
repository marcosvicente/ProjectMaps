from django.conf.urls import include, url
from django.contrib import admin

from core.views import Index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'$', Index.as_view() , name='index'),

]

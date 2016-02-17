# -*- encoding: utf-8 -*-

from django.contrib import admin

from .models import Viagem, Combustivel, Destino, Origem


class OrigemAdmin(admin.ModelAdmin):
    fields = ['cidade', 'bairro', 'endereco']


class DestinoAdmin(admin.ModelAdmin):
    fields = ['cidade', 'bairro', 'endereco']


class CombustivelAdmin(admin.ModelAdmin):
    fields = ['combustivel', 'preco']


class ViagemAdmin(admin.ModelAdmin):
    fields = ['nome', 'slug', 'combustivel', 'origem', 'destino']
    #prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Viagem, ViagemAdmin)
admin.site.register(Combustivel, CombustivelAdmin)
admin.site.register(Destino, DestinoAdmin)
admin.site.register(Origem, OrigemAdmin)

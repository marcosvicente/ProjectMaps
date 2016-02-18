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
    list_display = [
        'nome',
        'combustivel',
        'origem',
        'destino',
        'quilometros',
        'total_preco'
    ]

    # O valor do nome é inserido no slug
    prepopulated_fields = {'slug': ('nome',)}

    # lista de post por pagina
    list_per_page = 25
admin.site.register(Viagem, ViagemAdmin)
admin.site.register(Combustivel, CombustivelAdmin)
admin.site.register(Destino, DestinoAdmin)
admin.site.register(Origem, OrigemAdmin)

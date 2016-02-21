# -*- encoding: utf-8 -*-
from django import forms

from .models import Viagem, Origem, Destino, Combustivel


# Form, para inserir dadso no banco de dados da tabela Viagem
class ViagemForm(forms.ModelForm):

    class Meta:
        model = Viagem
        fields = "__all__"

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        return nome

    def clean_combustivel(self):
        combustivel = self.cleaned_data.get('combustivel')
        return combustivel

    def clean_origem(self):
        origem = self.cleaned_data.get('origem')
        return origem

    def clean_destino(self):
        destino = self.cleaned_data.get('destino')
        return destino

    def clean_quilometros(self):
        quilometros = self.cleaned_data.get('quilometros')

        if not quilometros > 0:
            raise forms.ValidationError("Digite um numero maior que 0")
        return quilometros

    def clean_total_preco(self):
        total_preco = self.cleaned_data.get('total_preco')

        # Validadação para numero ser maior de 0
        if not total_preco > 0:
            raise forms.ValidationError("Digite um numero maior que 0")
        return total_preco


class OrigemForm(forms.ModelForm):
    class Meta:
        model = Origem
        fields = "__all__"


class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = "__all__"


class CombustivelForm(forms.ModelForm):
    class Meta:
        model = Combustivel
        fields = "__all__"

# -*- encoding: utf-8 -*-
from django import forms


from .models import Viagem


# Form, para inserir dadso no banco de dados da tabela Viagem
class ViagemForm(forms.ModelForm):

    class Meta:
        model = Viagem
        fields = "__all__"

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        return nome

    def clean_quilometros(self):
        quilometros = self.cleaned_data.get('quilometros')
        return quilometros

    def clean_total_preco(self):
        total_preco = self.cleaned_data.get('total_preco')

        # Validadação para numero ser maior de 0
        if not total_preco > 0:
            raise forms.ValidationError("Digite um numero maior que 0")
        return total_preco

    def clean_slug(self):
        # o valor do field nome e redirecionando para o slug
        slug = self.cleaned_data.get('name')
        return slug

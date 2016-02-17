from __future__ import unicode_literals

from django.db import models

COMBUSTIVEL = (
    ('g', 'gasolina'),
    ('a', 'alcool'),
    ('d', 'diesel'),
)


class Origem(models.Model):
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)


class Destino(models.Model):
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)


class Combustivel(models.Model):
    combustivel = models.CharField(
        max_length=50,
        choices=COMBUSTIVEL,
        default="g"
    )
    preco = models.FloatField()


class Viagem(models.Model):
    combustivel = models.OneToOneField(
        Combustivel,
    )
    origem = models.OneToOneField(
        Origem,
    )
    destino = models.OneToOneField(
        Destino,
        on_delete=models.CASCADE
    )

from __future__ import unicode_literals

from django.db import models

COMBUSTIVEL = (
    ('g', 'gasolina'),
    ('a', 'alcool'),
    ('d', 'diesel'),
)


class Local(models.Model):
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)


class Origem(models.Model):
    nome = models.CharField(max_length=50)


class Destino(models.Model):
    nome = models.CharField(max_length=50)


class Combustivel(models.Model):
    combustivel = models.CharField(
        max_length=10,
        choices=COMBUSTIVEL,
        default="g"
    )
    preco = models.FloatField()

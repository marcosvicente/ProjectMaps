from __future__ import unicode_literals

from django.db import models

COMBUSTIVEL = (
    ('g', 'gasolina')
    ('a','alcool')
    ('d', 'diesel')
)


class Local(models.Model):
    cidade = models.Model()
    bairro = models.Model()
    endereco = models.Model()


class Origem(models.Model):
    nome = models.CharField()


class Destino(models.Model):
    nome = models.CharField()


class Combustivel(models.Model):
    combustivel = models.CharField(
        choices=COMBUSTIVEL, default="g"
    )

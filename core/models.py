# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

COMBUSTIVEL = (
    ('Gasolina', 'gasolina'),
    ('Alcool', 'alcool'),
    ('Diesel', 'diesel'),
)


class Origem(models.Model):
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)

    def __str__(self):
        return self.cidade


class Destino(models.Model):
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)

    def __str__(self):
        return self.cidade


class Combustivel(models.Model):
    combustivel = models.CharField(
        max_length=50,
        choices=COMBUSTIVEL,
        default="GASOLINA"
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return self.combustivel


class Viagem(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField()

    combustivel = models.OneToOneField(
        Combustivel,
    )
    origem = models.OneToOneField(
        Origem,
    )
    destino = models.OneToOneField(
        Destino,
    )
    quilometros = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return "Origem : {},  Destino: {}, Combustivel:  {}".format(
            self.origem,
            self.destino,
            self.combustivel)


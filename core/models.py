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
    preco = models.FloatField()

    def __str__(self):
        return self.combustivel


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

    def __str__(self):
        return "Origem : {},  Destino: {}, Combustivel:  {}".format(
            self.origem,
            self.destino,
            self.combustivel)


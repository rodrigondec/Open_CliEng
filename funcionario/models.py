from django.db import models
from equipamento.models import Equipamento


class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    qualificacoes = models.ManyToManyField(Equipamento, related_name='qualificados')

    def __str__(self):
        return self.nome

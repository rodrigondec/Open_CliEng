from django.db import models
from equipment.models import Equipment


class Funcionario(models.Model):
    nome = models.CharField(max_length=200)

    cpf = models.CharField(max_length=11)
    qualificacoes = models.ManyToManyField(Equipment, related_name='functionaries_qualified')

    def __str__(self):
        return self.nome


class Qualificacao(models.Model):
    OPERAR = 'OP'
    CALIBRAR = 'CA'
    MANUTENCAO = 'MA'

    TYPE_CHOICES = (
        (OPERAR, "Operar"),
        (CALIBRAR, "Calibrar"),
        (MANUTENCAO, "Manutenção"),
    )


from django.db import models
from equipamento.models import Equipamento


class Qualificacao(models.Model):
    CALIBRAR = 'CA'
    MANUTENCAO = 'MA'

    TYPE_CHOICES = (
        (CALIBRAR, "Calibrar"),
        (MANUTENCAO, "Realizar manutenção"),
    )

    equipamento = models.ForeignKey(Equipamento, related_name="qualificacoes")
    tipo = models.CharField(max_length=2, choices=TYPE_CHOICES, default=CALIBRAR)

    class Meta:
        unique_together = ('equipamento', 'tipo',)

    def __str__(self):
        return "{} {}".format(self.tipo, self.equipamento.nome)


class Responsavel(models.Model):
    nome = models.CharField(max_length=200)
    qualificacoes = models.ManyToManyField(Qualificacao, related_name='qualificados')

    def __str__(self):
        return self.nome


class TecnicoResponsavel(Responsavel):
    cpf = models.CharField(max_length=11)


class EmpresaResponsavel(Responsavel):
    cnpj = models.CharField(max_length=20)


class Manutencao(models.Model):
    equipamento = models.ForeignKey(Equipamento)
    responsavel = models.ForeignKey(Responsavel)
    descricao = models.TextField(max_length=200)

    data_realizada = models.DateTimeField('data realizada', null=True)

class ManutencaoPreventiva(Manutencao):
    data_agendada = models.DateTimeField('data agendada')

    def __str__(self):
        return "Preventiva para {} por {}".format(self.equipamento, self.responsavel)

class ManutencaoCalibragem(Manutencao):

    def __str__(self):
        return "Calibragem para {} por {}".format(self.equipamento, self.responsavel)


class ManutencaoCorretiva(Manutencao):

    def __str__(self):
        return "Corretiva para {} por {}".format(self.equipamento, self.responsavel)
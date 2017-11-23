from django.db import models
from core.models import Responsavel
from equipamento.models import Equipamento


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

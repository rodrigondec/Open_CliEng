from django.db import models
from core.models import Responsavel
from equipamento.models import Equipamento
from polymorphic.models import PolymorphicModel


class Manutencao(PolymorphicModel):
    equipamento = models.ForeignKey(Equipamento)
    responsavel = models.ForeignKey(Responsavel)
    descricao = models.TextField(max_length=200, null=True, blank=True)

    data_realizada = models.DateTimeField('data realizada', null=True, blank=True)

    @property
    def tipo(self):
        return "Manutencao"

class ManutencaoPreventiva(Manutencao):
    data_agendada = models.DateTimeField('data agendada')

    @property
    def tipo(self):
        return "Preventiva"

    def __str__(self):
        return "Preventiva para {} por {}".format(self.equipamento, self.responsavel)


class ManutencaoCalibragem(Manutencao):
    @property
    def tipo(self):
        return "Calibragem"

    def __str__(self):
        return "Calibragem para {} por {}".format(self.equipamento, self.responsavel)


class ManutencaoCorretiva(Manutencao):
    @property
    def tipo(self):
        return "Corretiva"

    def __str__(self):
        return "Corretiva para {} por {}".format(self.equipamento, self.responsavel)

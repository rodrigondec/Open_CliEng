from django.db import models
from djmoney.models.fields import MoneyField
from local.models import Setor
# from manutencao.models import TecnicoResponsavel


class Equipamento(models.Model):
    nome = models.CharField(max_length=50)
    num_serie = models.CharField(max_length=100)
    ano_fabricacao = models.DateField("Ano fabricacao")
    data_aquisicao = models.DateField('Data aquisição')
    fabricante = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    setor = models.ForeignKey(Setor, related_name='equipamentos')
    custo = MoneyField(max_digits= 8, decimal_places=2, default_currency='BRL')
    historico = models.TextField(max_length=800)
    manual = models.TextField(max_length=800)
    # responsavel = models.ForeignKey(TecnicoResponsavel, related_name='equipamentos')

    def __str__(self):
        return self.nome


class Contrato(models.Model):
    equipamento = models.OneToOneField(Equipamento, related_name='contrato', primary_key=True)
    descricao = models.TextField(max_length=800, null=True)

    def __str__(self):
        return "Contrato do equipamento {}".format(self.equipamento.nome)
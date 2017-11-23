from django.contrib.auth.models import User
from django.db import models
from equipamento.models import Equipamento


# class PerfilUsuario(models.Model):
#     usuario = models.OneToOneField(User)
    # qualificacoes = models.ManyToManyField(Equipamento, related_name='qualificados')


class Responsavel(models.Model):
    pass


class EmpresaResponsavel(Responsavel):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=20)


class TecnicoResponsavel(Responsavel):
    usuario = models.OneToOneField(User)
    # cpf = models.CharField(max_length=11)
    qualificacoes = models.ManyToManyField(Equipamento, related_name='tecnicos_qualificados')


class Funcionario(models.Model):
    usuario = models.OneToOneField(User)
    # cpf = models.CharField(max_length=11)
    qualificacoes = models.ManyToManyField(Equipamento, related_name='funcionarios_qualificados')

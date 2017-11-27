from django.contrib.auth.models import User
from django.db import models



# class PerfilUsuario(models.Model):
#     usuario = models.OneToOneField(User)
    # qualificacoes = models.ManyToManyField(Equipamento, related_name='qualificados')


class Responsavel(models.Model):
    pass


class EmpresaResponsavel(Responsavel):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class TecnicoResponsavel(Responsavel):
    usuario = models.OneToOneField(User)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.usuario.username

from equipamento.models import Equipamento

class Funcionario(models.Model):
    usuario = models.OneToOneField(User)
    cpf = models.CharField(max_length=11)
    qualificacoes = models.ManyToManyField(Equipamento, related_name='funcionarios_qualificados')

    def __str__(self):
        return self.usuario.username
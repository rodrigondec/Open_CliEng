from django.contrib.auth.models import User
from django.db import models
from polymorphic.models import PolymorphicModel


class Responsavel(PolymorphicModel):
    pass


class EmpresaResponsavel(Responsavel):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    telefone = models.CharField(max_length=10)

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

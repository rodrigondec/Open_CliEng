from django.db import models
from equipment.models import Equipment


class Responsavel(models.Model):
    pass


class ResponsavelTecnico(Responsavel):
    pass


class ResponsavelEmpresa(Responsavel):
    pass


class Maintenance(models.Model):
    equipment = models.ForeignKey(Equipment)
    responsavel = models.OneToOneField(Responsavel)
    description = models.TextField(max_length=200)

    date = models.DateTimeField('date realized')

    def __str__(self):
        return "Maintenance for {} equipment.".format(self.equipment.name)


class Preventive(Maintenance):
    pass


class Calibration(Maintenance):
    pass


class Corrective(Maintenance):
    pass

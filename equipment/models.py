from django.db import models
from location.models import Sector

class Equipment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    buy_date = models.DateTimeField('date bought')
    maintenance_freq = models.IntegerField(default=0)

    sector = models.ForeignKey(Sector, related_name='equipments')

    def __str__(self):
        return self.name


class Contract(models.Model):
    equipment = models.OneToOneField(Equipment, related_name='contract', primary_key=True)
    description = models.TextField(max_length=800)

    def __str__(self):
        return "Contract for {} equipment.".format(self.equipment.name)
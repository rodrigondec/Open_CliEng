from django.db import models
from equipment.models import Equipment


class Maintenance(models.Model):
    PREVENTIVE = 'PV'
    OTHER = 'OT'

    TYPE_CHOICES = (
        (PREVENTIVE, 'Preventiva'),
        (OTHER, 'Outra'),
    )

    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    category = models.CharField(max_length=2, choices=TYPE_CHOICES, default=PREVENTIVE)
    date = models.DateTimeField('date realized')

    def __str__(self):
        return "Maintenance for {} equipment.".format(self.equipment.name)

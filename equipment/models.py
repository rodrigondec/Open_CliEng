from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    buy_date = models.DateTimeField('date bought')
    maintenance_freq = models.IntegerField(default=0)

    def __str__(self):
        return self.name


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


class Contract(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    description = models.TextField(max_length=800)

    def __str__(self):
        return "Contract for {} equipment.".format(self.equipment.name)
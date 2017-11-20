from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    buy_date = models.DateTimeField('date bought')

    def __str__(self):
        return self.name


class Contract(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    text = models.CharField(max_length=800)

    def __str__(self):
        return "Contract for {} equipment.".format(self.equipment.name)
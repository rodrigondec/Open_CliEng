from django.db import models
from equipment.models import Equipment

# Create your models here.
class Functionary(models.Model):
    CPF = 'CPF'
    CRM = 'CRM'

    IDENTITY_TYPE_CHOICES = (
        (CPF, CPF),
        (CRM, CRM),
    )

    name = models.CharField(max_length=200)

    identity_type = models.CharField(max_length=3, choices=IDENTITY_TYPE_CHOICES, default=CPF)
    identity = models.CharField(max_length=50)

    qualifications = models.ManyToManyField(Equipment, related_name='functionaries_qualified')

    def __str__(self):
        return self.name


# class Qualification(models.Model):
#     name = models.CharField(max_length=200)
#     equipment = models.OneToOneField(Equipment, related_name='qualification', primary_key=True)


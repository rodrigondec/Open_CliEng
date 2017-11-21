from django.db import models

# Create your models here.
class Predio(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.nome

class Setor(models.Model):
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
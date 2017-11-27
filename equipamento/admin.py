from django.contrib import admin
from .models import Equipamento, ContratoProprio, ContratoComodato

# Register your models here.
admin.site.register(Equipamento)
admin.site.register(ContratoProprio)
admin.site.register(ContratoComodato)

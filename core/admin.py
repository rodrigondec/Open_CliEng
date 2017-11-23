from django.contrib import admin
from .models import EmpresaResponsavel, TecnicoResponsavel, Funcionario

# Register your models here.
admin.site.register(EmpresaResponsavel)
admin.site.register(TecnicoResponsavel)
admin.site.register(Funcionario)

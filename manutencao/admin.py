from django.contrib import admin
from .models import TecnicoResponsavel, EmpresaResponsavel, Qualificacao, ManutencaoPreventiva, ManutencaoCalibragem, ManutencaoCorretiva

# Register your models here.
admin.site.register(Qualificacao)
admin.site.register(TecnicoResponsavel)
admin.site.register(EmpresaResponsavel)
admin.site.register(ManutencaoPreventiva)
admin.site.register(ManutencaoCalibragem)
admin.site.register(ManutencaoCorretiva)
# admin.site.register()
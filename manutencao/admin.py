from django.contrib import admin
from .models import ManutencaoPreventiva, ManutencaoCalibragem, ManutencaoCorretiva

# Register your models here.
admin.site.register(ManutencaoPreventiva)
admin.site.register(ManutencaoCalibragem)
admin.site.register(ManutencaoCorretiva)
# admin.site.register()
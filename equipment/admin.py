from django.contrib import admin
from .models import Equipment, Contract, Maintenance

# Register your models here.
admin.site.register(Equipment)
admin.site.register(Contract)
admin.site.register(Maintenance)

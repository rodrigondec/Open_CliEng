import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Open_Clineng.settings")
django.setup()

from equipamento.models import Equipamento

a = Equipamento()
a.num_serie = 0
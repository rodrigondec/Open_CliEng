export DJANGO_SETTINGS_MODULE=Open_Clineng.settings

import django
django.setup()
from equipamento.models import Equipamento

a = Equipamento()
a.num_serie = 0



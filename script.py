export DJANGO_SETTINGS_MODULE=Open_Clineng.settings

import django
django.setup()
from equipamento.models import Equipamento

a = Equipamento("Acelerador Lienar")
a.num_serie = 158943
a.reg_anvisa = 10405410012
a.ano_fabricacao = 2017-06-14
a.data_aquisicao = 2017-09-29
a.fabricante = "Varian"
a.modelo = "CLINAC IX"
a.setor = "Radiologia"
a.custo = 800000
a.historico = "Comprado em 2017-09-29" \n "Recebido em 2017-10-20. Setor: Almoxarifado" \n "Instalado em 2017-11-04. Setor: Radiologia" 
a.manual = 
a.responsavel = 
a.contrato = 

b = Equipamento("Tomógrado Computadorizado")
b.num_serie = 166857
b.reg_anvisa = 10295030060
b.ano_fabricacao = 2017-06-14
b.data_aquisicao = 2017-09-29
b.fabricante = "Toshiba"
b.modelo = "ASTEION VR TSX-021A"
b.setor = "Radiologia"
b.custo = 2000000
b.historico = "Comprado em 2017-09-29" \n "Recebido em 2017-10-20. Setor: Almoxarifado" \n "Instalado em 2017-11-04. Setor: Radiologia" 
b.manual = 
b.responsavel = 
b.contrato = 

c = Equipamento("Gama Câmara")
c.num_serie = 25998
c.reg_anvisa = 10234230140 
c.ano_fabricacao = 2017-06-14
c.data_aquisicao = 2017-09-29
c.fabricante = "Siemens"
c.modelo = "Gama Câmara c.cam"
c.setor = "Radiologia"
c.custo = 725000
c.historico = "Comprado em 2017-09-29" \n "Recebido em 2017-10-20. Setor: Almoxarifado" \n "Instalado em 2017-11-04. Setor: Radiologia" 
c.manual = 
c.responsavel = 
c.contrato = 

d = Equipamento("Ultrassom")
d.num_serie = 25998
d.reg_anvisa = 10234230209
d.ano_fabricacao = 2017-06-14
d.data_aquisicao = 2017-09-29
d.fabricante = "Siemens"
d.modelo = "ACUSON X600"
d.setor = "Radiologia"
d.custo = 47000
d.historico = "Comprado em 2017-09-29" \n "Recebido em 2017-10-20. Setor: Almoxarifado" \n "Instalado em 2017-11-04. Setor: Radiologia" 
d.manual = 
d.responsavel = 
d.contrato = 

e = Equipamento("Bisturi Elétrico")
e.num_serie = 8890
e.reg_anvisa = 10214670025 
e.ano_fabricacao = 2017-06-14
e.data_aquisicao = 2017-09-29
e.fabricante = "Deltronix"
e.modelo = "SEG 100+"
e.setor = "Radiologia"
e.custo = 2500
e.historico = "Comprado em 2017-09-29" \n "Recebido em 2017-10-10. Setor: Almoxarifado" \n "Instalado em 2017-11-04. Setor: Centro Cirúrgico" 
e.manual = 
e.responsavel = 
e.contrato = 

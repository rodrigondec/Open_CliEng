import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Open_Clineng.settings")
django.setup()

from django.contrib.auth.models import User
from core.models import Responsavel, TecnicoResponsavel, Funcionario, EmpresaResponsavel
from equipamento.models import Equipamento, Contrato, ContratoProprio, ContratoComodato
from local.models import Predio, Setor


# users = User.objects.all()
# for user in users:
#     print(user)
rodrigo = User(username='rodrigondec', email='rodrigondec@gmail.com', password='pbkdf2_sha256$36000$JiznF9X6FCu6$LshWCb2ht8vF8FakEPBmrs5SPY7or8xMTKzBDWHh5yE=', is_staff=True, is_superuser=True)
rodrigo.save()
mateusc = User(username='mateusc', email='mateusc@gmail.com', password='pbkdf2_sha256$36000$JiznF9X6FCu6$LshWCb2ht8vF8FakEPBmrs5SPY7or8xMTKzBDWHh5yE=', is_staff=True, is_superuser=True)
mateusc.save()

# responsaveis = Responsavel.objects.all()
# tecnico = TecnicoResponsavel.objects.get(id=1)
tecnico_user = User(username='tecnico_x', password='pbkdf2_sha256$36000$JiznF9X6FCu6$LshWCb2ht8vF8FakEPBmrs5SPY7or8xMTKzBDWHh5yE=')
tecnico_user.save()
tecnico = TecnicoResponsavel(usuario=tecnico_user, cpf=0)
tecnico.save()
#
# funcionario = Funcionario.objects.get(id=1)
funcionario_user = User(username='funcionario_x', password='pbkdf2_sha256$36000$JiznF9X6FCu6$LshWCb2ht8vF8FakEPBmrs5SPY7or8xMTKzBDWHh5yE=')
funcionario_user.save()
funcionario = Funcionario(usuario=funcionario_user, cpf=0)
funcionario.save()
#
# empresa = EmpresaResponsavel.objects.get(id=2)
empresa = EmpresaResponsavel(nome="Empresa X", cnpj=0, email='empresa_x@gmail.com', telefone='0')
empresa.save()
#
predio = Predio(nome="Predio X", descricao="bla")
predio.save()
radiologia = Setor(nome="Radiologia", predio=predio)
radiologia.save()
# radiologia = Setor.objects.get(id=1)


# a = Equipamento.objects.get(id=1)
a = Equipamento(nome="Acelerador Lienar")
a.num_serie = 158943
a.reg_anvisa = 10405410012
a.ano_fabricacao = "2017-06-14"
a.data_aquisicao = "2017-09-29"
a.fabricante = "Varian"
a.modelo = "CLINAC IX"
a.setor = radiologia
a.custo = 800000
a.historico = "Comprado em 2017-09-29\n Recebido em 2017-10-20. Setor: Almoxarifado\n Instalado em 2017-11-04. Setor: Radiologia"
# a.manual =
a.responsavel = tecnico
ac = ContratoProprio(descricao="texto contrato", valor=0)
ac.save()
a.contrato = ac
a.save()

b = Equipamento(nome="Tomógrado Computadorizado")
b.num_serie = 166857
b.reg_anvisa = 10295030060
b.ano_fabricacao = "2017-06-14"
b.data_aquisicao = "2017-09-29"
b.fabricante = "Toshiba"
b.modelo = "ASTEION VR TSX-021A"
b.setor = radiologia
b.custo = 2000000
b.historico = "Comprado em 2017-09-29 \n Recebido em 2017-10-20. Setor: Almoxarifado \n Instalado em 2017-11-04. Setor: Radiologia"
# b.manual =
b.responsavel = tecnico
bc = ContratoComodato(descricao="texto contrato", valor=500, empresa=empresa)
bc.save()
b.contrato = bc
b.save()

c = Equipamento(nome="Gama Câmara")
c.num_serie = 25998
c.reg_anvisa = 10234230140 
c.ano_fabricacao = "2017-06-14"
c.data_aquisicao = "2017-09-29"
c.fabricante = "Siemens"
c.modelo = "Gama Câmara c.cam"
c.setor = radiologia
c.custo = 725000
c.historico = "Comprado em 2017-09-29 \n Recebido em 2017-10-20. Setor: Almoxarifado \n Instalado em 2017-11-04. Setor: Radiologia"
# c.manual =
c.responsavel = tecnico
cc = ContratoComodato(descricao="texto contrato", valor=800, empresa=empresa)
cc.save()
c.contrato = cc
c.save()

d = Equipamento(nome="Ultrassom")
d.num_serie = 25998
d.reg_anvisa = 10234230209
d.ano_fabricacao = "2017-06-14"
d.data_aquisicao = "2017-09-29"
d.fabricante = "Siemens"
d.modelo = "ACUSON X600"
d.setor = radiologia
d.custo = 47000
d.historico = "Comprado em 2017-09-29 \n Recebido em 2017-10-20. Setor: Almoxarifado \n Instalado em 2017-11-04. Setor: Radiologia"
# d.manual =
d.responsavel = tecnico
dc = ContratoProprio(descricao="texto contrato", valor=0)
dc.save()
d.contrato = dc
d.save()

e = Equipamento(nome="Bisturi Elétrico")
e.num_serie = 8890
e.reg_anvisa = 10214670025 
e.ano_fabricacao = "2017-06-14"
e.data_aquisicao = "2017-09-29"
e.fabricante = "Deltronix"
e.modelo = "SEG 100+"
e.setor = radiologia
e.custo = 2500
e.historico = "Comprado em 2017-09-29 \n Recebido em 2017-10-10. Setor: Almoxarifado \n Instalado em 2017-11-04. Setor: Centro Cirúrgico"
# e.manual =
e.responsavel = tecnico
ec = ContratoProprio(descricao="texto contrato", valor=0)
ec.save()
e.contrato = ec
e.save()

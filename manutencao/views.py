from django.shortcuts import render

from .models import Manutencao

def index(request):
    context = {'manutencoes': None}
    return render(request, 'manutencao/index.html', context)

def manutencao_detalhes(request, manutencaoid):
    manutencao = Manutencao.objects.get(pk=manutencaoid)
    return render(request, 'manutencao/detalhes.html', manutencao=manutencao)

from django.shortcuts import render

from .models import Manutencao

def manutencao_detalhes(request, manutencaoid):
    manutencao = Manutencao.objects.get(pk=manutencaoid)
    return render(request, 'manutencao_detalhes.html', manutencao=manutencao)

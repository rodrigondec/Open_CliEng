from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Manutencao


@login_required
def index(request):
    context = {'manutencoes': None}
    return render(request, 'manutencao/index.html', context)


@login_required
def manutencao_detalhes(request, manutencaoid):
    manutencao = Manutencao.objects.get(pk=manutencaoid)
    return render(request, 'manutencao/detalhes.html', manutencao=manutencao)

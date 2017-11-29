from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Equipamento, Contrato
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    equipamentos = Equipamento.objects.all()
    context = {'equipamentos': equipamentos, "usuario_autenticado": request.user.is_authenticated()}
    return render(request, 'equipamento/index.html', context)


@login_required
def detalhar(request, equipamentoid):
    equipamento = get_object_or_404(Equipamento, pk=equipamentoid)
    context = {'equipamento': equipamento, "usuario_autenticado": request.user.is_authenticated()}
    return render(request, 'equipamento/equipamento_detalhes.html', context)


@login_required
def detalhar_contrato(request, contratoid):
    contrato = get_object_or_404(Contrato, pk=contratoid)
    context = {'contrato': contrato, "usuario_autenticado": request.user.is_authenticated()}
    return render(request, 'equipamento/contrato_detalhes.html', context)

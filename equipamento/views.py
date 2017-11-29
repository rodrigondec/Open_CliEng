from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Equipamento, ContratoProprio
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {'equipamentos': Equipamento.objects.all()}
    return render(request, 'equipamento/index.html', context)

@login_required
def detalhar(request, equipamentoid):
    equipamento = get_object_or_404(Equipamento, pk=equipamentoid)
    return render(request, 'equipamento/detalhar_equipamento.html', {'equipamento': equipamento})

@login_required
def detalhar_contrato(request, contratoid):
    contrato = get_object_or_404(ContratoProprio, pk=contratoid)
    return render(request, 'equipamento/detalhar_contrato.html', {'contrato': contrato})

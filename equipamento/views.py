from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Equipamento, ContratoProprio


def index(request):
    context = {'equipamentos': Equipamento.objects.all()}
    return render(request, 'equipamento/index.html', context)


def detalhar(request, equipamentoid):
    equipamento = get_object_or_404(Equipamento, pk=equipamentoid)
    return render(request, 'equipamento/detalhar_equipamento.html', {'equipamento': equipamento})


def detalhar_contrato(request, contratoid):
    contrato = get_object_or_404(ContratoProprio, pk=contratoid)
    return render(request, 'equipamento/detalhar_contrato.html', {'contrato': contrato})

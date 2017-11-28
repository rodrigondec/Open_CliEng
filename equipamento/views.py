from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipamento


def index(request):
    context = {'equipamentos': Equipamento.objects.all()}
    return render(request, 'equipamento/index.html', context)


def detalhar_equipamento(request):
    return HttpResponse("detalhar equipamento")


def detalhar_contrato(request):
    return HttpResponse("detalhar contrato")

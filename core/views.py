from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Funcionario, TecnicoResponsavel
from manutencao.models import Manutencao
from equipamento.models import Equipamento


@login_required
def index(request):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated()

    context['funcionarios'] = Funcionario.objects.all()
    context['tecnicos'] = TecnicoResponsavel.objects.all()
    context['manutencoes'] = Manutencao.objects.all()
    context['equipamentos'] = Equipamento.objects.all()

    return render(request, 'core/index.html', context)


@login_required
def detalhar_funcionario(request, funcionarioid):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated()

    context['funcionario'] = get_object_or_404(Funcionario, pk=funcionarioid)

    return render(request, 'core/funcionario_detalhes.html', context)


@login_required
def detalhar_tecnico(request, tecnicoid):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated()

    context['tecnico'] = get_object_or_404(TecnicoResponsavel, pk=tecnicoid)

    return render(request, 'core/tecnico_detalhes.html', context)

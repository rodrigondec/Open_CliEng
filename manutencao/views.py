from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Manutencao


@login_required
def index(request):
    context = {}
    context["usuario_autenticado"] = request.user.is_authenticated()

    context['manutencoes'] = Manutencao.objects.all()

    return render(request, 'manutencao/index.html', context)


@login_required
def manutencao_detalhes(request, manutencaoid):
    context = {}
    context["usuario_autenticado"] = request.user.is_authenticated()

    context['manutencao'] = get_object_or_404(Manutencao, pk=manutencaoid)

    return render(request, 'manutencao/manutencao_detalhes.html', context)

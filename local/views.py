from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {'locais': None}
    return render(request, 'local/index.html', context)
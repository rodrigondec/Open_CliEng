from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    context = {"usuario_autenticado": request.user.is_authenticated()}
    return render(request, 'core/index.html', context)

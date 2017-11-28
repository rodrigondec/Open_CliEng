from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'locais': None}
    return render(request, 'local/index.html', context)
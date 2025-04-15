from django.shortcuts import render
from .models import Evento

# Create your views here.
def index(request):
    return render(request, "index.html")

def timeline(request):
    eventos = Evento.objects.all().order_by('ordem')
    context = {'eventos': eventos}

    return render(request, 'routes/timeline.html', context)
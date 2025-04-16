from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Evento, Descricao

# Create your views here.
def index(request):
    return render(request, "index.html")

def timeline(request):
    eventos = Evento.objects.all().order_by('ordem')
    context = {'eventos': eventos}

    return render(request, 'routes/timeline.html', context)

def descricao(request, evento_id):
    try:
        descricao = Descricao.objects.get(evento_id=evento_id)
        return render(request, 'routes/descricao.html', {'descricao': descricao})
    except Descricao.DoesNotExist:
        # Se não houver descrição, redireciona de volta para a timeline
        return render(request, 'routes/descricao.html', {
            'mensagem': 'Descrição ainda não disponível para este evento.',
            'evento': get_object_or_404(Evento, id=evento_id)
        })
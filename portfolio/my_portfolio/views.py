from django.shortcuts import render, get_object_or_404
from .models import Evento, Descricao
from django.db.models.functions import ExtractYear

# Create your views here.
def index(request):
    return render(request, "index.html")

def timeline(request):
    # Obtém todos os anos que têm eventos (baseado na data_inicio), ordenados do mais recente para o mais antigo
    anos_disponiveis = Evento.objects.annotate(
        ano_inicio=ExtractYear('data_inicio')
    ).values_list('ano_inicio', flat=True).distinct().order_by('-ano_inicio')
    
    # Se não houver eventos, retorna contexto vazio
    if not anos_disponiveis:
        return render(request, 'routes/timeline.html', {'eventos': []})
    
    # Obtém o ano da query string ou usa o ano mais recente como padrão
    ano_selecionado = request.GET.get('ano')
    
    if ano_selecionado:
        ano_atual = int(ano_selecionado)
        # Verifica se o ano selecionado existe nos eventos
        if ano_atual not in anos_disponiveis:
            ano_atual = anos_disponiveis[0]  # Usa o ano mais recente se o selecionado não existir
    else:
        # Usa o ano mais recente como padrão
        ano_atual = anos_disponiveis[0]
    
    # Obtém os eventos do ano selecionado, ordenados pela data de início (mais recente primeiro)
    eventos = Evento.objects.filter(
        data_inicio__year=ano_atual
    ).order_by('data_inicio')  # Adicionado o '-' para ordenar de forma decrescente
    
    context = {
        'eventos': eventos,
        'anos_disponiveis': anos_disponiveis,
        'ano_atual': ano_atual
    }

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

def projetos(request):
    eventos = Evento.objects.all().order_by('-data_inicio')
    return render(request, 'routes/projetos.html', {'eventos': eventos})
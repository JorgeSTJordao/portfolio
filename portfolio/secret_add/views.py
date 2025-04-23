from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from functools import wraps
from my_portfolio.models import Evento, Descricao
from .forms import SecretLoginForm, EventoForm, DescricaoForm

def secret_required(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.session.get('secret_authenticated'):
            return redirect('secret_add:login')
        return view_func(request, *args, **kwargs)
    return _wrapped

def login_view(request):
    """
    - GET: exibe o formulário vazio.
    - POST: valida email+senha contra settings; se OK, seta sessão e redireciona.
    """
    if request.session.get('secret_authenticated'):
        return redirect('secret_add:add')

    if request.method == 'POST':
        form = SecretLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            if (email == settings.TIMELINE_USER and 
                password == settings.TIMELINE_PASS):
                request.session['secret_authenticated'] = True
                return redirect('secret_add:add')
            
            messages.error(request, 'Credenciais inválidas')
    else:
        form = SecretLoginForm()

    return render(request, 'login.html', {'form': form})

@secret_required
def add_event_view(request):
    """
    - GET: exibe dois formulários vazios (Evento + Descrição).
    - POST: valida ambos; se OK, salva Evento e Descricao, então redireciona para o mesmo form limpo.
    """
    if request.method == 'POST':
        evento_form = EventoForm(request.POST)
        descricao_form = DescricaoForm(request.POST)

        if evento_form.is_valid() and descricao_form.is_valid():
            evento = evento_form.save()
            descricao = descricao_form.save(commit=False)
            descricao.evento = evento
            descricao.save()
            
            messages.success(request, 'Evento adicionado com sucesso!')
            return redirect('secret_add:add')

    else:
        evento_form = EventoForm()
        descricao_form = DescricaoForm()

    return render(request, 'add.html', {
        'evento_form': evento_form,
        'descricao_form': descricao_form,
    })

from django import forms
from my_portfolio.models import Evento, Descricao

class SecretLoginForm(forms.Form):
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'})
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'})
    )

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'resumo', 'data_inicio', 'data_conclusao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
            'resumo': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-md', 'rows': 3}),
            'data_inicio': forms.DateInput(attrs={'class': 'w-full px-3 py-2 border rounded-md', 'type': 'date'}),
            'data_conclusao': forms.DateInput(attrs={'class': 'w-full px-3 py-2 border rounded-md', 'type': 'date'}),
        }

class DescricaoForm(forms.ModelForm):
    class Meta:
        model = Descricao
        fields = ['conteudo_html']
        widgets = {'conteudo': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-md', 'rows': 15}),} 
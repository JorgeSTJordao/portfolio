from django.db import models

# Create your models here.

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    data_inicio = models.DateField()
    concluido = models.BooleanField(default=False)
    ano = models.IntegerField()
    ordem = models.IntegerField(default=0)

    class Meta:
        ordering = ['ano', 'ordem']

    def __str__(self):
        return f"{self.titulo} ({self.data_inicio})"

class Descricao(models.Model):
    evento_id = models.ForeignKey(Evento, null=True, blank=True, on_delete=models.CASCADE)
    conteudo_html = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Descrição do evento {self.evento_id.id}"

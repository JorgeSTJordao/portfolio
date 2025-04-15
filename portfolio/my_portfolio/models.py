from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    concluido = models.BooleanField(default=False)
    ano = models.IntegerField()
    ordem = models.IntegerField(default=0)

    class Meta:
        ordering = ['ano', 'ordem']

    def __str__(self):
        return f"{self.titulo} ({self.data_inicio})"

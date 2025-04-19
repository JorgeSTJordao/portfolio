from django.db import models

# Create your models here.

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    data_inicio = models.DateField()
    data_conclusao = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-data_inicio']  # Ordena por data de início, mais recente primeiro

    def __str__(self):
        return f"{self.titulo} ({self.data_inicio})"

    @property
    def esta_concluido(self):
        return self.data_conclusao is not None

class Descricao(models.Model):
    evento_id = models.ForeignKey(Evento, null=True, blank=True, on_delete=models.CASCADE)
    conteudo_html = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Descrição do evento {self.evento_id.id}"

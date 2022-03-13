from django.db import models
from django.contrib.auth.models import User


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    local = models.TextField()
    data_evento = models.DateTimeField(blank=True,
                                       null=True,
                                       verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True,
                                        verbose_name='Data de Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # Definição do nome da tabela
        db_table = 'evento'

    def __str__(self):
        return self.titulo

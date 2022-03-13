from django.shortcuts import render, HttpResponse
from .models import Evento

# Create your views here.


def ObterLocalEvento(request, titulo_evento):
    _evento = Evento.objects.get(titulo=titulo_evento)
    resposta = f'Este é local do evento: {_evento.local}'
    print(len(resposta))
    return HttpResponse(resposta)

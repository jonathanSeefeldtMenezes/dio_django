from django.shortcuts import render, HttpResponse
from .models import Evento

# Create your views here.

#def index(request):
#    return redirect('/agenda')


def obter_local_evento(request, titulo_evento):
    _evento = Evento.objects.get(titulo=titulo_evento)
    resposta = f'Este é local do evento: {_evento.local}'
    print(len(resposta))
    return HttpResponse(resposta)


def listar_eventos(request):
    url_login = 'http://127.0.0.1:8000/admin/login/?next=/admin/'

    try:
        usuario = request.user
        eventos = Evento.objects.filter(usuario=usuario)
        dados = {'eventos': eventos, 'usuario': usuario}
        return render(request, 'agenda.html', dados)

    except BaseException as ex:
        mensagem_erro = f'Mensagem de erro: {ex}.'

        if 'AnonymousUser' in str(ex):
            return HttpResponse(f'{mensagem_erro}<br>'
                                f'<a href="{url_login}">Faça o Login</a>')
        else:
            return HttpResponse(mensagem_erro)


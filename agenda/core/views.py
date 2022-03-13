from django.shortcuts import render, HttpResponse, redirect
from .models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

@login_required(login_url='/login/')
def obter_local_evento(request, titulo_evento):
    _evento = Evento.objects.get(titulo=titulo_evento)
    resposta = f'Este é local do evento: {_evento.local}'
    print(len(resposta))
    return HttpResponse(resposta)


@login_required(login_url='/login/')
def listar_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos, 'usuario': usuario}
    return render(request, 'agenda.html', dados)


def logar_usuario(request):
    return render(request, 'login.html')


def logar_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request,'Usuário/Senha incorretos.')

    return redirect('/')


def deslogar_usuario(request):
    logout(request)
    return redirect('/')

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
def evento_listar_todos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos, 'usuario': usuario}
    return render(request, 'agenda.html', dados)


def usuario_logar(request):
    return render(request, 'login.html')


def usuario_logar_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário/Senha incorretos.')

    return redirect('/')


def usuario_logout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def evento(request):
    dados = {}

    evento_id = request.GET.get('id')
    if evento_id:
        dados['evento'] = Evento.objects.get(id=evento_id)

    return render(request, 'evento.html', dados)


def evento_submit(request):
    if request.POST:
        evento = Evento(
            titulo=request.POST.get('titulo'),
            descricao=request.POST.get('descricao'),
            local=request.POST.get('local'),
            data_evento=request.POST.get('data-evento'),
            usuario=request.user
        )

        if request.POST.get('evento_id'):
            evento.id = request.POST.get('evento_id')

        evento.save()

    return redirect('/')


@login_required(login_url='/login/')
def evento_excluir(request, id_evento):
    evento = Evento.objects.get(id=id_evento)

    if evento.usuario == request.user:
        evento.delete()
    else:
        messages.error(request, 'Evento selecionado inválido.')

    return redirect('/')

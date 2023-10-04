from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais')
            return redirect('/usuarios/cadastro')

        if len(senha) < 7:  # Corrigi para 7, já que você quer 7 ou mais dígitos
            messages.add_message(request, constants.ERROR, 'Sua senha deve ter 7 ou mais dígitos')
            return redirect('/usuarios/cadastro')

        # Verificar se o usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'O nome de usuário já está em uso')
            return redirect('/usuarios/cadastro')

        try:
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, 'Cadastro feito com sucesso !')
        except Exception as e:  # Capturando exceção para depuração
            print(str(e))
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema, contate um administrador')

        return redirect('/usuarios/cadastro')

def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('/') #vai dar erro por enquanto
        else:
         messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
         return redirect('/usuarios/login')
     

from django.shortcuts import render

# Create your views here.
# Aqui você define as funções ou classes que processam as requisições e retornam respostas.


def home(request):
    return render(request, 'SAC/pages/home.html',
                  context={'name': 'Plac'})


def login(request):
    return render(request, 'SAC\pages\login-page.html',
                  context={'name': 'Login'})


def register(request):
    return render(request, 'SAC/pages/register.html',
                  context={'name': 'Cadastro'})

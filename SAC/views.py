from django.shortcuts import render, redirect
from .models import Reclamacao
from django.contrib.auth.decorators import login_required

# Create your views here.
# Aqui você define as funções ou classes que processam as requisições e retornam respostas.


def home(request):
    return render(request, 'SAC/pages/home.html',
                  context={'name': 'Plac'})


def login(request):
    return render(request, 'SAC/pages/login-page.html',
                  context={'name': 'Login'})


def register(request):
    return render(request, 'SAC/pages/register.html',
                  context={'name': 'Cadastro'})


def complaint(request):
    return render(request, 'SAC/partials/sac.html',
                  context={'name': 'Sac'})


def suggestion(request):
    return render(request, 'SAC/partials/suggestion.html',
                  context={'name': 'Sugestão'})


def homepage(request):
    return render(request, 'SAC/partials/homepage.html',
                  context={'name': 'Reclamações'})

# Adicionar getattr nas reclamações

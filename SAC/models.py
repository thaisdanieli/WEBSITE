from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Aqui você define as tabelas do banco de dados como classes Python.


class User(models.Model):


class Reclamacao(models.Model):
    user = models.ForeignKey(User, verbose_name=_(
        "Usuario"), on_delete=models.CASCADE)

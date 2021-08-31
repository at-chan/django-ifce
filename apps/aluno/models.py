from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do aluno')

    cpf = models.CharField(max_length=11, help_text='CPF do aluno')

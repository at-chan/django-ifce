from django.db import models

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=120,help_text='Nome do Professor')
    cpf = models.CharField(max_length=12,help_text='CPF',default='')
    formacao = models.CharField(max_length=200,help_text='Formação',default='')
    birthdate = models.DateField(blank=True, null=True)  
    email = models.CharField(max_length=100,help_text='E-mail',default='')
   

class Meta:
    ordering=['-id']


def __str__(self):
    return self.nome
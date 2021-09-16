from django.contrib import admin
from aluno.models import Aluno
# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
       list_display = ['nome', 'cpf', 'user']
       
admin.site.register(Aluno,AlunoAdmin)
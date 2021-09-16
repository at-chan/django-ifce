from django.contrib import admin

# Register your models here.
from .models import Professor

class ProfessorAdmin(admin.ModelAdmin):
       list_display = ['nome', 'cpf', 'formacao']

admin.site.register(Professor,ProfessorAdmin)
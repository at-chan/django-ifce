from django.contrib import admin
from django.urls import include, path
from apps.core import views


app_name = 'aluno'

from . import views

urlpatterns = [

    #adicionando a view do core

    path('novo/',views.AddAluno,name='add_aluno'),
    path('',views.HomeView.as_view(),name='home'),
    path('lista/',views.ListAlunosView.as_view(),name='lista_alunos')
]

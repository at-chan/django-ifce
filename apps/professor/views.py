from django.shortcuts import render,redirect, get_list_or_404,get_object_or_404
from django.contrib import messages
from professor.forms import ProfessorForm
# Create your views here.


def AddProfessor(request):
    template_name = 'professor/add_professor.html'
    context = {}
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados salvos com sucesso!")
        else:
            messages.error(request, "Erro")
    form = ProfessorForm()
    context['form'] = form
    return render(request,template_name,context)
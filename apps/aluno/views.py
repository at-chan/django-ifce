from django.shortcuts import render,redirect, get_list_or_404,get_object_or_404
from aluno.models  import Aluno
from django.contrib import messages
from aluno.forms import AlunoForm
from django.views.generic import TemplateView,CreateView,ListView


# Create your views here.



def AddAluno(request):
    template_name = 'aluno/add_aluno.html'
    context = {}
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            # f = form.save(commit=False)
            form.save()
            messages.success(request, "Usuário salvo com sucesso!")
        else:
            messages.error(request, "Erro ao salvar dados!")
    form = AlunoForm()
    context['form'] = form
    return render(request,template_name,context)


class HomeView(TemplateView):
   template_name = 'aluno/lista_alunos.html'


class ListAlunosView(ListView):
   model = Aluno
   template_name = 'aluno/lista_alunos.html'
   context_object_name = 'alunos'
   paginate_by = 6

   def get_queryset(self):
       return Aluno.objects.all().order_by('-id')

def deleteAluno(request, id_aluno):
    aluno = Aluno.objects.get(id=id_aluno)
    aluno.delete()
    messages.success(request, "Aluno deletado com sucesso!")
    return redirect('aluno:lista_alunos')

def edit_aluno(request, id_aluno):
    template_name = 'aluno/add_aluno.html'
    context = {}
    aluno = get_object_or_404(Aluno, pk=id_aluno)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, "Aluno editado com sucesso!")
            return redirect('aluno:lista_alunos')
    form = AlunoForm(instance=aluno)
    context['form'] = form
    return render(request, template_name, context)

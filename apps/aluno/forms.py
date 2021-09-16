from django import forms
from aluno.models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        # fields = ['nome','cpf','email','data_nasc','user']
        fields = '__all__'
        
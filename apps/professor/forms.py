from django import forms
from professor.models import Professor


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
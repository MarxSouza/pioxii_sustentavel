from django import forms
from .models import Pesquisa

class PesquisaForm(forms.ModelForm):
    class Meta:
        model = Pesquisa
        fields = '__all__'
        widgets = {
            'estado_civil': forms.RadioSelect,
            'nacionalidade': forms.RadioSelect
        }
from django import forms
from .models import Pesquisa

class Form1(forms.ModelForm):
    class Meta:
        model = Pesquisa
        fields = ['entrevistadores','nome','sexo','idade','escolaridade',
                  'a_pergunta_1','a_pergunta_2','a_pergunta_3',
                  'a_pergunta_4','a_pergunta_5','a_pergunta_6',
                  'a_pergunta_7','a_pergunta_8','a_pergunta_9']
        widgets = {'a_pergunta_1': forms.RadioSelect,'a_pergunta_2': forms.RadioSelect,
                   'a_pergunta_3': forms.RadioSelect,'a_pergunta_4': forms.RadioSelect,
                   'a_pergunta_5': forms.RadioSelect,'a_pergunta_6': forms.RadioSelect,
                   'a_pergunta_7': forms.RadioSelect,'a_pergunta_8': forms.RadioSelect,
                   'a_pergunta_9': forms.RadioSelect}

class Form2(forms.ModelForm):
    class Meta:
        model = Pesquisa
        fields = ['entrevistadores','nome','sexo','idade','escolaridade',
                  'b_pergunta_1','b_pergunta_2','b_pergunta_3',
                  'b_pergunta_4','b_pergunta_5','b_pergunta_6']
        widgets = {'b_pergunta_1': forms.RadioSelect,'b_pergunta_2': forms.RadioSelect,
                   'b_pergunta_3': forms.RadioSelect,'b_pergunta_4': forms.RadioSelect,
                   'b_pergunta_5': forms.RadioSelect}

class Form3(forms.ModelForm):
    class Meta:
        model = Pesquisa
        fields = ['entrevistadores','nome','sexo','idade','funcao',
                  'c_pergunta_1','c_pergunta_2','c_pergunta_3','c_pergunta_4']
        widgets = {'c_pergunta_2': forms.RadioSelect, 'c_pergunta_3': forms.RadioSelect,
                   'c_pergunta_4': forms.RadioSelect}
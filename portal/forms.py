from django import forms

Cores = (
    ('azul', 'Azul'),
    ('rosa', 'Rosa'),
    ('verde', 'Verde'),
)
Times = (
    ('vasco', 'Vasco'),
    ('botafogo', 'Botafogo'),
    ('palmeiras', 'Palmeiras'),
)
Faixas =(
    ('de 10 a 14 anos', 'De 10 a 14 anos'),
    ('de 14 a 18 anos', 'De 10 a 18 anos'),
    ('de 18 a 25 anos', 'De 18 a 25 anos'),
    ('de 25 a 40 anos', 'De 25 a 40 anos'),
    ('de 40 a 60 anos', 'De 40 a 60 anos'),
    ('de 60 a 90 anos', 'De 60 a 90 anos'),
    ('de 90 a 999 anos', 'De 90 a 999 anos'),
)
class Pesquisa(forms.Form):
    seu_nome = forms.CharField(required=True, label='Seu Nome', max_length=100)
    cores_favoritas = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Cores)
    time = forms.ChoiceField(label='Time do coração', widget=forms.Select, choices=Times)
    faixa_etaria = forms.ChoiceField(label='Faixa etaria', widget=forms.RadioSelect(), choices=Faixas)
from django.shortcuts import render, HttpResponseRedirect
from . import forms

def index(request):
    return render(request, 'portal/index.html', {})

def formulario(request):
    if request.method == 'POST':
        form = forms.Pesquisa(request.POST)
        if form.is_valid():
            return HttpResponseRedirect
    else:
        form = forms.Pesquisa
    return render(request, 'portal/formulario.html', {'form': form})

def grafico(request):
    return render(request, 'portal/grafico.html', {})

def sobre(request):
    return render(request, 'portal/sobre.html', {})

def baixarapp(request):
    pass
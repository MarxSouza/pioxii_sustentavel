from django.shortcuts import render, render_to_response, HttpResponseRedirect
from . import forms
from .models import Pesquisa

def index(request):
    return render_to_response('portal/index.html')

def formulario(request):
    if request.method == 'POST':
        form = forms.PesquisaForm(request.POST, request.FILES)
        if form.is_valid():
            pes = form.save()
            pes.save()
            return HttpResponseRedirect("/pesquisa/grafico/?form=save")
    else: 
        form = forms.PesquisaForm()
    return render(request, 'portal/formulario.html', {
        'form': form
    })

def grafico(request):
    respostas = Pesquisa.objects.count()
    solteiros = Pesquisa.objects.filter(estado_civil='solteiro(a)')
    casados = Pesquisa.objects.filter(estado_civil='casado(a)')
    separados = Pesquisa.objects.filter(estado_civil='separado(a)')
    viuvos = Pesquisa.objects.filter(estado_civil='viuvo(a)')    
    brasileiros = Pesquisa.objects.filter(nacionalidade='brasileiro(a)')
    naturalizados = Pesquisa.objects.filter(nacionalidade='brasileiro naturalizado(a)')
    estrangeiros = Pesquisa.objects.filter(nacionalidade='estrangeiro(a)')
    
    return render(request, 'portal/grafico.html', {
        'brasileiros': brasileiros, 'naturalizados': naturalizados,
        'estrangeiros':estrangeiros, 'solteiros':solteiros,
        'casados':casados, 'separados':separados, 'viuvos':viuvos, 
        'respostas':respostas
    })

def sobre(request):
    return render_to_response('portal/sobre.html')

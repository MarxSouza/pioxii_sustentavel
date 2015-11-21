# -*- coding: utf-8
from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Pesquisa

def index(request):
    return render_to_response('portal/index.html')

@login_required
def formularios(request):
    if request.method == 'POST':
        form_1 = forms.Form1(request.POST, request.FILES)
        form_2 = forms.Form2(request.POST, request.FILES)
        form_3 = forms.Form3(request.POST, request.FILES)
        if form_1.is_valid():
            pes = form_1.save()
            pes.save()
            return HttpResponseRedirect("/grafico/")
        if form_2.is_valid():
            pes = form_2.save()
            pes.save()
            return HttpResponseRedirect("/grafico/")
        if form_3.is_valid():
            pes = form_3.save()
            pes.save()
            return HttpResponseRedirect("/grafico/")
        
    else: 
        form_1 = forms.Form1()
        form_2 = forms.Form2()
        form_3 = forms.Form3()
    return render(request, 'portal/formularios.html', {
        'form_1': form_1,
        'form_2': form_2,
        'form_3': form_3,
    })

def grafico(request):
    #respostas = Pesquisa.objects.count()
    # -- Form 1
    #pergunta_1
    a_1_a = Pesquisa.objects.filter(a_pergunta_1='Nenhuma')
    a_1_b = Pesquisa.objects.filter(a_pergunta_1='1 a 5')
    a_1_c = Pesquisa.objects.filter(a_pergunta_1='6 a 10')
    a_1_d = Pesquisa.objects.filter(a_pergunta_1='11 a 15')
    a_1_e = Pesquisa.objects.filter(a_pergunta_1='Mais de 15')
    #pergunta_2
    a_2_a = Pesquisa.objects.filter(a_pergunta_2='Guarda')
    a_2_b = Pesquisa.objects.filter(a_pergunta_2='Descarta')
    a_2_c = Pesquisa.objects.filter(a_pergunta_2='Usa como saco de lixo')
    a_2_d = Pesquisa.objects.filter(a_pergunta_2='Outros')
    #pergunta_3
    a_3_a = Pesquisa.objects.filter(a_pergunta_3='Sim')
    a_3_b = Pesquisa.objects.filter(a_pergunta_2='Não')
    #pergunta_4
    a_4_a = Pesquisa.objects.filter(a_pergunta_4='Sim')
    a_4_b = Pesquisa.objects.filter(a_pergunta_4='Não')
    #pergunta_5
    a_5_a = Pesquisa.objects.filter(a_pergunta_5='Sempre')
    a_5_b = Pesquisa.objects.filter(a_pergunta_5='As vezes')
    #pergunta_6
    a_6_a = Pesquisa.objects.filter(a_pergunta_6='Sim')
    a_6_b = Pesquisa.objects.filter(a_pergunta_6='Não')    
    #pergunta_7
    a_7_a = Pesquisa.objects.filter(a_pergunta_7='Sim')
    a_7_b = Pesquisa.objects.filter(a_pergunta_7='Não')
    #pergunta_8
    a_8_a = Pesquisa.objects.filter(a_pergunta_8='Sim')
    a_8_b = Pesquisa.objects.filter(a_pergunta_8='Não')
    #pergunta_9
    a_9_a = Pesquisa.objects.filter(a_pergunta_9='Sim')
    a_9_b = Pesquisa.objects.filter(a_pergunta_9='Não')
    
    # -- Form 2
    #pergunta_1
    b_1_a = Pesquisa.objects.filter(b_pergunta_1='Descarta na pia')
    b_1_b = Pesquisa.objects.filter(b_pergunta_1='Envia para a reciclagem')
    b_1_c = Pesquisa.objects.filter(b_pergunta_1='Descarta em terreno baldio')
    #pergunta_2
    b_2_a = Pesquisa.objects.filter(b_pergunta_2='1 a 4')
    b_2_b = Pesquisa.objects.filter(b_pergunta_2='5 a 7')
    b_2_c = Pesquisa.objects.filter(b_pergunta_2='8 a 10')
    #pergunta_3
    b_3_a = Pesquisa.objects.filter(b_pergunta_3='Bom')
    b_3_b = Pesquisa.objects.filter(b_pergunta_3='Ótimo')
    b_3_c = Pesquisa.objects.filter(b_pergunta_3='Não faz diferença')
    #pergunta_4
    b_4_a = Pesquisa.objects.filter(b_pergunta_4='Sim')
    b_4_b = Pesquisa.objects.filter(b_pergunta_4='Não')
    #pergunta_5
    b_5_a = Pesquisa.objects.filter(b_pergunta_5='Sim')
    b_5_b = Pesquisa.objects.filter(b_pergunta_5='Não')
    b_5_c = Pesquisa.objects.filter(b_pergunta_5='Talvez')
    
    # -- Form 3
    #pergunta_2
    c_2_a = Pesquisa.objects.filter(c_pergunta_2='Biodegradável')
    c_2_b = Pesquisa.objects.filter(c_pergunta_2='Não biodegradável')
    #pergunta_3
    c_3_a = Pesquisa.objects.filter(c_pergunta_3='Sim')
    c_3_b = Pesquisa.objects.filter(c_pergunta_3='Não')
    #pergunta_4
    c_4_a = Pesquisa.objects.filter(c_pergunta_4='Sim')
    c_4_b = Pesquisa.objects.filter(c_pergunta_4='Não')
    
    return render(request, 'portal/grafico.html', {
        # -- Form 1
        'a_1_a':a_1_a,'a_1_b':a_1_b,'a_1_c':a_1_c,'a_1_d':a_1_d,'a_1_e':a_1_e,
        'a_2_a':a_2_a,'a_2_b':a_2_b,'a_2_c':a_2_c,'a_2_d':a_2_d,
        'a_3_a':a_3_a,'a_3_b':a_3_b,
        'a_4_a':a_4_a,'a_4_b':a_4_b,
        'a_5_a':a_5_a,'a_5_b':a_5_b,
        'a_6_a':a_6_a,'a_6_b':a_6_b,
        'a_7_a':a_7_a,'a_7_b':a_7_b,
        'a_8_a':a_8_a,'a_8_b':a_8_b,
        'a_9_a':a_9_a,'a_9_b':a_9_b,
        # -- Form 2
        'b_1_a':b_1_a,'a_1_b':b_1_b,'b_1_c':b_1_c,
        'b_2_a':b_2_a,'a_2_b':b_2_b,'b_2_c':b_2_c,
        'b_3_a':b_3_a,'a_3_b':b_3_b,'b_3_c':b_3_c,
        'b_4_a':b_4_a,'a_4_b':b_4_b,
        'b_5_a':b_5_a,'a_5_b':b_5_b,'b_5_c':b_5_c,
        # -- Form 3
        'c_2_a':c_2_a,'c_1_b':c_2_b,
        'c_3_a':c_3_a,'c_2_b':c_3_b,
        'c_4_a':c_4_a,'c_4_b':c_4_b,
    })

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
        form_2 = forms.Form1(request.POST, request.FILES)
        form_3 = forms.Form1(request.POST, request.FILES)
        if form_1.is_valid():
            pes = form_1.save(commit=False)
            pes.entrevistadores = request.user
            pes.save()
            return HttpResponseRedirect("/grafico/")
        if form_2.is_valid():
            pes = form_2.save(commit=False)
            pes.entrevistadores = request.user
            pes.save()
            return HttpResponseRedirect("/grafico/")
        if form_3.is_valid():
            pes = form_3.save(commit=False)
            pes.entrevistadores = request.user
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
    mas = Pesquisa.objects.filter(sexo='masculino')
    fem = Pesquisa.objects.filter(sexo='feminino')
    id_1 = Pesquisa.objects.filter(idade='menos de 20')
    id_2 = Pesquisa.objects.filter(idade='20 a 30')
    id_3 = Pesquisa.objects.filter(idade='30 a 40')
    id_4 = Pesquisa.objects.filter(idade='40 a 50')
    id_5 = Pesquisa.objects.filter(idade='mais de 50')
    nao = Pesquisa.objects.filter(escolaridade='não estudou')
    fun = Pesquisa.objects.filter(escolaridade='fundamental')
    med = Pesquisa.objects.filter(escolaridade='médio')
    sup = Pesquisa.objects.filter(escolaridade='superior')
    # -- Form 1
    #pergunta_1
    a_1_a = Pesquisa.objects.filter(a_pergunta_1='nenhuma')
    a_1_b = Pesquisa.objects.filter(a_pergunta_1='1 a 5')
    a_1_c = Pesquisa.objects.filter(a_pergunta_1='6 a 10')
    a_1_d = Pesquisa.objects.filter(a_pergunta_1='11 a 15')
    a_1_e = Pesquisa.objects.filter(a_pergunta_1='mais de 15')
    #pergunta_2
    a_2_a = Pesquisa.objects.filter(a_pergunta_2='guarda')
    a_2_b = Pesquisa.objects.filter(a_pergunta_2='descarta')
    a_2_c = Pesquisa.objects.filter(a_pergunta_2='usa como saco de lixo')
    a_2_d = Pesquisa.objects.filter(a_pergunta_2='outros')
    #pergunta_3
    a_3_a = Pesquisa.objects.filter(a_pergunta_3='sim')
    a_3_b = Pesquisa.objects.filter(a_pergunta_2='não')
    #pergunta_4
    a_4_a = Pesquisa.objects.filter(a_pergunta_4='sim')
    a_4_b = Pesquisa.objects.filter(a_pergunta_4='não')
    #pergunta_5
    a_5_a = Pesquisa.objects.filter(a_pergunta_5='sempre')
    a_5_b = Pesquisa.objects.filter(a_pergunta_5='as vezes')
    #pergunta_6
    a_6_a = Pesquisa.objects.filter(a_pergunta_6='sim')
    a_6_b = Pesquisa.objects.filter(a_pergunta_6='não')    
    #pergunta_7
    a_7_a = Pesquisa.objects.filter(a_pergunta_7='sim')
    a_7_b = Pesquisa.objects.filter(a_pergunta_7='não')
    #pergunta_8
    a_8_a = Pesquisa.objects.filter(a_pergunta_8='sim')
    a_8_b = Pesquisa.objects.filter(a_pergunta_8='não')
    #pergunta_9
    a_9_a = Pesquisa.objects.filter(a_pergunta_9='sim')
    a_9_b = Pesquisa.objects.filter(a_pergunta_9='não')
    
    # -- Form 2
    #pergunta_1
    b_1_a = Pesquisa.objects.filter(b_pergunta_1='descarta na pia')
    b_1_b = Pesquisa.objects.filter(b_pergunta_1='envia para a reciclagem')
    b_1_c = Pesquisa.objects.filter(b_pergunta_1='descarta em terreno baldio')
    #pergunta_2
    b_2_a = Pesquisa.objects.filter(b_pergunta_2='1 a 4')
    b_2_b = Pesquisa.objects.filter(b_pergunta_2='5 a 7')
    b_2_c = Pesquisa.objects.filter(b_pergunta_2='8 a 10')
    #pergunta_3
    b_3_a = Pesquisa.objects.filter(b_pergunta_3='bom')
    b_3_b = Pesquisa.objects.filter(b_pergunta_3='ótimo')
    b_3_c = Pesquisa.objects.filter(b_pergunta_3='não faz diferença')
    #pergunta_4
    b_4_a = Pesquisa.objects.filter(b_pergunta_4='sim')
    b_4_b = Pesquisa.objects.filter(b_pergunta_4='não')
    #pergunta_5
    b_5_a = Pesquisa.objects.filter(b_pergunta_5='sim')
    b_5_b = Pesquisa.objects.filter(b_pergunta_5='não')
    b_5_c = Pesquisa.objects.filter(b_pergunta_5='talvez')
    
    # -- Form 3
    #pergunta_2
    c_2_a = Pesquisa.objects.filter(c_pergunta_2='biodegradável')
    c_2_b = Pesquisa.objects.filter(c_pergunta_2='não biodegradável')
    #pergunta_3
    c_3_a = Pesquisa.objects.filter(c_pergunta_3='sim')
    c_3_b = Pesquisa.objects.filter(c_pergunta_3='não')
    #pergunta_4
    c_4_a = Pesquisa.objects.filter(c_pergunta_4='sim')
    c_4_b = Pesquisa.objects.filter(c_pergunta_4='não')
    
    return render(request, 'portal/grafico.html', {
        'mas':mas,'fem':fem, 
        'id_1':id_1,'id_2':id_2,
        'id_3':id_3,'id_4':id_4,
        'id_5':id_5, 'nao':nao,'fun':fun,
        'med':med,'sup':sup,                            
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

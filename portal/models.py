# -*- coding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Parte 1
sexos =         (('masculino', 'Masculino'), ('feminino','Feminino'),)
idades =         (('menos de 20','Menos de 20'),('de 20 a 30','de 20 a 30'),('de 30 a 40', 'de 30 a 40'),('de 40 a 50', 'de 40 a 50'), ('mais de 50','mais de 50'))
escolaridades = (('não estudou','Não Estudou'),('fundamental','Fundamental'),('médio','Médio'),('superior','Superior'),)
# Parte 2 
choices_1 =     (('nenhuma','Nenhuma'),('1 a 5','1 a 5'),('6 a 10','6 a 10'),('11 a 15','11 a 15'),('mais de 15','Mais de 15'),)
choices_2 =     (('guarda','Guarda'),('descarta','Descarta'),('usa como saco de lixo','Usa como saco de lixo'),('outros','Outros'),)
choices_3 =     (('sim','Sim'), ('não','Não'))
choices_4 =     (('sempre','Sempre'),('as vezes','As vezes'))
choices_5 =     (('descarta na pia','Descarta na pia'),('envia para a reciclagem','Envia para a reciclagem'), ('descarta em terreno baldio','Descarta em terreno baldio'),)
choices_6 =     (('1 a 4','1 a 4'),('5 a 7','5 a 7'),('8 a 10','8 a 10'),)
choices_7 =     (('bom','Bom'),('ótimo','Ótimo'),('não faz diferença','Não faz diferença'),)
choices_8 =     (('sim','Sim'), ('não','Não'), ('talvez','Talvez'),)
choices_9 =     (('biodegradável','Biodegradável'),('não biodegradável','Não biodegradável'),)

class Pesquisa(models.Model):
    #Parte 1
    entrevistadores = models.ForeignKey(User,default='')
    nome = models.CharField('Nome do Entrevistado:',max_length=100,default='')
    sexo = models.CharField('Sexo:',choices=sexos, max_length=10,default='')
    idade = models.CharField(default='', max_length=100, choices=idades)
    escolaridade = models.CharField('Escolaridade:',choices=escolaridades, max_length=100,default='')
    funcao = models.CharField('Função no estabelecimento:', max_length=100,default='')
    
    #Parte 2
    # -- Form 1 --
    a_pergunta_1 = models.CharField('1. Quantas sacolas plásticas, em média, você obtem semanalmente?',choices=choices_1, max_length=100,default='')
    a_pergunta_2 = models.CharField('2. O que você faz com as sacolas plásticas?',choices=choices_2, max_length=100, default='')
    a_pergunta_3 = models.CharField('3. Você conhece as sacolas retornáveis?',choices=choices_3, max_length=100, default='')
    a_pergunta_4 = models.CharField('4. Se sim, você usa sacolas retornáveis?',choices=choices_3, max_length=100,default='')
    a_pergunta_5 = models.CharField('5. Qual frequência?',choices=choices_4, max_length=100,default='')
    a_pergunta_6 = models.CharField('6. Você acha que consumo e descarte inapropriados das sacolas plásticas, causam prejuízos ao meio ambiente?',choices=choices_3, max_length=100,default='')
    a_pergunta_7 = models.CharField('7. Você tem conhecimento do projeto de Lei que visa a proibição da distribuição das sacolas plásticas pelos estabelecimentos comerciais?',choices=choices_3, max_length=100,default='')
    a_pergunta_8 = models.CharField('8. Se sim, concorda?',choices=choices_3, max_length=100,default='')
    a_pergunta_9 = models.CharField('9. Você gostou de participar dessa pesquisa?',choices=choices_3, max_length=100,default='')
    # -- Form 2 --
    b_pergunta_1 = models.CharField('1. Qual destino que você dá ao óleo depois do seu uso?', choices=choices_5, max_length=900,default='')
    b_pergunta_2 = models.CharField('2. De 1 a 10 qual a importância do reaproveitamento do óleo?', choices=choices_6, max_length=100,default='')
    b_pergunta_3 = models.CharField('3. O que você acha de ter em sua comunidade um espaço para recolher esse tipo de resíduo?', choices=choices_7, max_length=100,default='')
    b_pergunta_4 = models.CharField('4. Vocẽ sabia que da pra reaproveitar o óleo?', choices=choices_3, max_length=100,default='')
    b_pergunta_5 = models.CharField('5. Você usaria em seu dia-a-dia um sabão produzido a partir do óleo?', choices=choices_8, max_length=100,default='')
    b_pergunta_6 = models.TextField('6. Qual a sua opinião com relação a esse assunto?',default='')
    # -- Form 3 --
    c_pergunta_2 = models.CharField('2. Qual tipo de sacola é comprada?', choices=choices_9, max_length=100, default='')
    c_pergunta_3 = models.CharField('3. Você tem conhecimento do projeto de Lei que visa a proibição da distribuição das sacolas plásticas pelos estabelecimentos comerciais?', choices=choices_3, max_length=100, default='')
    c_pergunta_4 = models.CharField('4. Se sim, concorda?', choices=choices_3, max_length=100, default='')
    
    def __str__(self):
        return self.nome
    
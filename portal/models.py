from django.db import models

nacionalidades = (
    ('brasileiro(a)', 'Brasileiro(a)'),
    ('brasileiro naturalizado(a)', 'Brasileiro naturalizado(a)'),
    ('estrangeiro(a)', 'Estrangeiro(a)'),
)
estados_civis = (
    ('solteiro(a)','Solteiro(a)'),
    ('casado(a)','Casado(a)'),
    ('separado(a)','Separado(a)'),
    ('viúvo(a)','Viúvo(a)')
)

class Pesquisa(models.Model):
    seu_nome = models.CharField('Nome Completo:',max_length=100)
    estado_civil = models.CharField('1. Qual a sua nacionalidade?',default='Brasileiro(a)', max_length=100, choices=estados_civis)
    nacionalidade = models.CharField('2. Qual o seu estado civil?',default='Solteiro(a)', max_length=100, choices=nacionalidades)
    
    def __str__(self):
        return self.seu_nome
    
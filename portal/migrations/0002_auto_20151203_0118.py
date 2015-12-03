# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_1',
            field=models.CharField(choices=[('nenhuma', 'Nenhuma'), ('1 a 5', '1 a 5'), ('6 a 10', '6 a 10'), ('11 a 15', '11 a 15'), ('mais de 15', 'Mais de 15')], verbose_name='1. Quantas sacolas plásticas, em média, você obtem semanalmente?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_2',
            field=models.CharField(choices=[('guarda', 'Guarda'), ('descarta', 'Descarta'), ('usa como saco de lixo', 'Usa como saco de lixo'), ('outros', 'Outros')], verbose_name='2. O que você faz com as sacolas plásticas?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_3',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], verbose_name='3. Você conhece as sacolas retornáveis?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_4',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], verbose_name='4. Se sim, você usa sacolas retornáveis?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_5',
            field=models.CharField(choices=[('sempre', 'Sempre'), ('as vezes', 'As vezes')], verbose_name='5. Qual frequência?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_6',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], verbose_name='6. Você acha que consumo e descarte inapropriados das sacolas plásticas, causam prejuízos ao meio ambiente?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_7',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], verbose_name='7. Você tem conhecimento do projeto de Lei que visa a proibição da distribuição das sacolas plásticas pelos estabelecimentos comerciais?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_8',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], verbose_name='8. Se sim, concorda?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_9',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], verbose_name='9. Você gostou de participar dessa pesquisa?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='b_pergunta_1',
            field=models.CharField(choices=[('descarta na pia', 'Descarta na pia'), ('envia para a reciclagem', 'Envia para a reciclagem'), ('descarta em terreno baldio', 'Descarta em terreno baldio')], verbose_name='1. Qual destino que você dá ao óleo depois do seu uso?', max_length=900, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='b_pergunta_2',
            field=models.CharField(choices=[('1 a 4', '1 a 4'), ('5 a 7', '5 a 7'), ('8 a 10', '8 a 10')], verbose_name='2. De 1 a 10 qual a importância do reaproveitamento do óleo?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='b_pergunta_3',
            field=models.CharField(choices=[('bom', 'Bom'), ('ótimo', 'Ótimo'), ('não faz diferença', 'Não faz diferença')], verbose_name='3. O que você acha de ter em sua comunidade um espaço para recolher esse tipo de resíduo?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='b_pergunta_4',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], verbose_name='4. Vocẽ sabia que da pra reaproveitar o óleo?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='b_pergunta_5',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não'), ('talvez', 'Talvez')], verbose_name='5. Você usaria em seu dia-a-dia um sabão produzido a partir do óleo?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='b_pergunta_6',
            field=models.TextField(verbose_name='6. Qual a sua opinião com relação a esse assunto?', default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='c_pergunta_2',
            field=models.CharField(choices=[('biodegradável', 'Biodegradável'), ('não biodegradável', 'Não biodegradável')], verbose_name='2. Qual tipo de sacola é comprada?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='c_pergunta_3',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], verbose_name='3. Você tem conhecimento do projeto de Lei que visa a proibição da distribuição das sacolas plásticas pelos estabelecimentos comerciais?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='c_pergunta_4',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], verbose_name='4. Se sim, concorda?', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='entrevistadores',
            field=models.ForeignKey(default='', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='escolaridade',
            field=models.CharField(choices=[('não estudou', 'Não Estudou'), ('fundamental', 'Fundamental'), ('médio', 'Médio'), ('superior', 'Superior')], verbose_name='Escolaridade:', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='funcao',
            field=models.CharField(verbose_name='Função no estabelecimento:', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='idade',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='nome',
            field=models.CharField(verbose_name='Nome do Entrevistado:', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='sexo',
            field=models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], verbose_name='Sexo:', max_length=10, default=''),
        ),
    ]

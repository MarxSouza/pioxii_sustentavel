# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0021_auto_20151120_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_1',
            field=models.CharField(choices=[('nenhuma', 'Nenhuma'), ('1 a 5', '1 a 5'), ('6 a 10', '6 a 10'), ('11 a 15', '11 a 15'), ('mais de 15', 'Mais de 15')], max_length=100, verbose_name='1. Quantas sacolas plásticas, em média, você obtem semanalmente?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_2',
            field=models.CharField(choices=[('guarda', 'Guarda'), ('descarta', 'Descarta'), ('usa como saco de lixo', 'Usa como saco de lixo'), ('outros', 'Outros')], max_length=100, verbose_name='2. O que você faz com as sacolas plásticas?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_3',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], max_length=100, verbose_name='3. Você conhece as sacolas retornáveis?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_4',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], max_length=100, verbose_name='4. Se sim, você usa sacolas retornáveis?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_5',
            field=models.CharField(choices=[('sempre', 'Sempre'), ('as vezes', 'As vezes')], max_length=100, verbose_name='5. Qual frequência?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_6',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], max_length=100, verbose_name='6. Você acha que consumo e descarte inapropriados das sacolas plásticas, causam prejuízos ao meio ambiente?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_7',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], max_length=100, verbose_name='7. Você tem conhecimento do projeto de Lei que visa a proibição da distribuição das sacolas plásticas pelos estabelecimentos comerciais?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_8',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], max_length=100, verbose_name='8. Se sim, concorda?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_9',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], max_length=100, verbose_name='9. Você gostou de participar dessa pesquisa?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='b_pergunta_1',
            field=models.CharField(choices=[('descarta na pia', 'Descarta na pia'), ('envia para a reciclagem', 'Envia para a reciclagem'), ('descarta em terreno baldio', 'Descarta em terreno baldio')], max_length=900, verbose_name='1. Qual destino que você dá ao óleo depois do seu uso?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='b_pergunta_2',
            field=models.CharField(choices=[('1 a 4', '1 a 4'), ('5 a 7', '5 a 7'), ('8 a 10', '8 a 10')], max_length=100, verbose_name='2. De 1 a 10 qual a importância do reaproveitamento do óleo?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='b_pergunta_3',
            field=models.CharField(choices=[('bom', 'Bom'), ('ótimo', 'Ótimo'), ('não faz diferença', 'Não faz diferença')], max_length=100, verbose_name='3. O que você acha de ter em sua comunidade um espaço para recolher esse tipo de resíduo?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='b_pergunta_4',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], max_length=100, verbose_name='4. Vocẽ sabia que da pra reaproveitar o óleo?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='b_pergunta_5',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não'), ('talvez', 'Talvez')], max_length=100, verbose_name='5. Você usaria em seu dia-a-dia um sabão produzido a partir do óleo?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='b_pergunta_6',
            field=models.TextField(verbose_name='6. Qual a sua opinião com relação a esse assunto?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='c_pergunta_2',
            field=models.CharField(choices=[('biodegradável', 'Biodegradável'), ('não biodegradável', 'Não biodegradável')], max_length=100, verbose_name='2. Qual tipo de sacola é comprada?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='c_pergunta_3',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], max_length=100, verbose_name='3. Você tem conhecimento do projeto de Lei que visa a proibição da distribuição das sacolas plásticas pelos estabelecimentos comerciais?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='c_pergunta_4',
            field=models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], max_length=100, verbose_name='4. Se sim, concorda?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='escolaridade',
            field=models.CharField(choices=[('analfabeto', 'Analfabeto'), ('ensino fundamental 1', 'Somente o Ensino Fundamental 2'), ('ensino fundamental 2', 'Somente o Ensino Fundamental 2'), ('ensino médio', 'Ensino Médio'), ('ensino superior', 'Ensino Superior')], max_length=100, verbose_name='Escolaridade:'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='funcao',
            field=models.CharField(max_length=100, verbose_name='Função no estabelecimento:'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome do Entrevistado:'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='sexo',
            field=models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], max_length=10, verbose_name='Sexo:'),
        ),
    ]

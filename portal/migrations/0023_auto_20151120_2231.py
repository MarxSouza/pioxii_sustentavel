# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0022_auto_20151120_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesquisa',
            name='b_pergunta_1',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='b_pergunta_2',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='b_pergunta_3',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='b_pergunta_4',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='b_pergunta_5',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='b_pergunta_6',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='c_pergunta_2',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='c_pergunta_3',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='c_pergunta_4',
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_1',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'1. Quantas sacolas pl\xc3\xa1sticas, em m\xc3\xa9dia, voc\xc3\xaa obtem semanalmente?', choices=[(b'nenhuma', b'Nenhuma'), (b'1 a 5', b'1 a 5'), (b'6 a 10', b'6 a 10'), (b'11 a 15', b'11 a 15'), (b'mais de 15', b'Mais de 15')]),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_2',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'2. O que voc\xc3\xaa faz com as sacolas pl\xc3\xa1sticas?', choices=[(b'guarda', b'Guarda'), (b'descarta', b'Descarta'), (b'usa como saco de lixo', b'Usa como saco de lixo'), (b'outros', b'Outros')]),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_3',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'3. Voc\xc3\xaa conhece as sacolas retorn\xc3\xa1veis?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')]),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_4',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'4. Se sim, voc\xc3\xaa usa sacolas retorn\xc3\xa1veis?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')]),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_5',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'5. Qual frequ\xc3\xaancia?', choices=[(b'sempre', b'Sempre'), (b'as vezes', b'As vezes')]),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_6',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'6. Voc\xc3\xaa acha que consumo e descarte inapropriados das sacolas pl\xc3\xa1sticas, causam preju\xc3\xadzos ao meio ambiente?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')]),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_7',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'7. Voc\xc3\xaa tem conhecimento do projeto de Lei que visa a proibi\xc3\xa7\xc3\xa3o da distribui\xc3\xa7\xc3\xa3o das sacolas pl\xc3\xa1sticas pelos estabelecimentos comerciais?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')]),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_8',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'8. Se sim, concorda?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')]),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='a_pergunta_9',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'9. Voc\xc3\xaa gostou de participar dessa pesquisa?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')]),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='entrevistadores',
            field=models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='escolaridade',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Escolaridade:', choices=[(b'analfabeto', b'Analfabeto'), (b'ensino fundamental 1', b'Somente o Ensino Fundamental 2'), (b'ensino fundamental 2', b'Somente o Ensino Fundamental 2'), (b'ensino m\xc3\xa9dio', b'Ensino M\xc3\xa9dio'), (b'ensino superior', b'Ensino Superior')]),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='funcao',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Fun\xc3\xa7\xc3\xa3o no estabelecimento:'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='nome',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Nome do Entrevistado:'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='sexo',
            field=models.CharField(default=b'', max_length=10, verbose_name=b'Sexo:', choices=[(b'masculino', b'Masculino'), (b'feminino', b'Feminino')]),
        ),
    ]

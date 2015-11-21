# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pesquisa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'', max_length=100, verbose_name=b'Nome do Entrevistado:')),
                ('sexo', models.CharField(default=b'', max_length=10, verbose_name=b'Sexo:', choices=[(b'masculino', b'Masculino'), (b'feminino', b'Feminino')])),
                ('idade', models.IntegerField(default=b'')),
                ('escolaridade', models.CharField(default=b'', max_length=100, verbose_name=b'Escolaridade:', choices=[(b'analfabeto', b'Analfabeto'), (b'ensino fundamental 1', b'Somente o Ensino Fundamental 2'), (b'ensino fundamental 2', b'Somente o Ensino Fundamental 2'), (b'ensino m\xc3\xa9dio', b'Ensino M\xc3\xa9dio'), (b'ensino superior', b'Ensino Superior')])),
                ('funcao', models.CharField(default=b'', max_length=100, verbose_name=b'Fun\xc3\xa7\xc3\xa3o no estabelecimento:')),
                ('a_pergunta_1', models.CharField(default=b'', max_length=100, verbose_name=b'1. Quantas sacolas pl\xc3\xa1sticas, em m\xc3\xa9dia, voc\xc3\xaa obtem semanalmente?', choices=[(b'nenhuma', b'Nenhuma'), (b'1 a 5', b'1 a 5'), (b'6 a 10', b'6 a 10'), (b'11 a 15', b'11 a 15'), (b'mais de 15', b'Mais de 15')])),
                ('a_pergunta_2', models.CharField(default=b'', max_length=100, verbose_name=b'2. O que voc\xc3\xaa faz com as sacolas pl\xc3\xa1sticas?', choices=[(b'guarda', b'Guarda'), (b'descarta', b'Descarta'), (b'usa como saco de lixo', b'Usa como saco de lixo'), (b'outros', b'Outros')])),
                ('a_pergunta_3', models.CharField(default=b'', max_length=100, verbose_name=b'3. Voc\xc3\xaa conhece as sacolas retorn\xc3\xa1veis?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')])),
                ('a_pergunta_4', models.CharField(default=b'', max_length=100, verbose_name=b'4. Se sim, voc\xc3\xaa usa sacolas retorn\xc3\xa1veis?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')])),
                ('a_pergunta_5', models.CharField(default=b'', max_length=100, verbose_name=b'5. Qual frequ\xc3\xaancia?', choices=[(b'sempre', b'Sempre'), (b'as vezes', b'As vezes')])),
                ('a_pergunta_6', models.CharField(default=b'', max_length=100, verbose_name=b'6. Voc\xc3\xaa acha que consumo e descarte inapropriados das sacolas pl\xc3\xa1sticas, causam preju\xc3\xadzos ao meio ambiente?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')])),
                ('a_pergunta_7', models.CharField(default=b'', max_length=100, verbose_name=b'7. Voc\xc3\xaa tem conhecimento do projeto de Lei que visa a proibi\xc3\xa7\xc3\xa3o da distribui\xc3\xa7\xc3\xa3o das sacolas pl\xc3\xa1sticas pelos estabelecimentos comerciais?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')])),
                ('a_pergunta_8', models.CharField(default=b'', max_length=100, verbose_name=b'8. Se sim, concorda?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')])),
                ('a_pergunta_9', models.CharField(default=b'', max_length=100, verbose_name=b'9. Voc\xc3\xaa gostou de participar dessa pesquisa?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')])),
                ('b_pergunta_1', models.CharField(default=b'', max_length=900, verbose_name=b'1. Qual destino que voc\xc3\xaa d\xc3\xa1 ao \xc3\xb3leo depois do seu uso?', choices=[(b'descarta na pia', b'Descarta na pia'), (b'envia para a reciclagem', b'Envia para a reciclagem'), (b'descarta em terreno baldio', b'Descarta em terreno baldio')])),
                ('b_pergunta_2', models.CharField(default=b'', max_length=100, verbose_name=b'2. De 1 a 10 qual a import\xc3\xa2ncia do reaproveitamento do \xc3\xb3leo?', choices=[(b'1 a 4', b'1 a 4'), (b'5 a 7', b'5 a 7'), (b'8 a 10', b'8 a 10')])),
                ('b_pergunta_3', models.CharField(default=b'', max_length=100, verbose_name=b'3. O que voc\xc3\xaa acha de ter em sua comunidade um espa\xc3\xa7o para recolher esse tipo de res\xc3\xadduo?', choices=[(b'bom', b'Bom'), (b'\xc3\xb3timo', b'\xc3\x93timo'), (b'n\xc3\xa3o faz diferen\xc3\xa7a', b'N\xc3\xa3o faz diferen\xc3\xa7a')])),
                ('b_pergunta_4', models.CharField(default=b'', max_length=100, verbose_name=b'4. Voc\xe1\xba\xbd sabia que da pra reaproveitar o \xc3\xb3leo?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')])),
                ('b_pergunta_5', models.CharField(default=b'', max_length=100, verbose_name=b'5. Voc\xc3\xaa usaria em seu dia-a-dia um sab\xc3\xa3o produzido a partir do \xc3\xb3leo?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o'), (b'talvez', b'Talvez')])),
                ('b_pergunta_6', models.TextField(default=b'', verbose_name=b'6. Qual a sua opini\xc3\xa3o com rela\xc3\xa7\xc3\xa3o a esse assunto?')),
                ('c_pergunta_2', models.CharField(default=b'', max_length=100, verbose_name=b'2. Qual tipo de sacola \xc3\xa9 comprada?', choices=[(b'biodegrad\xc3\xa1vel', b'Biodegrad\xc3\xa1vel'), (b'n\xc3\xa3o biodegrad\xc3\xa1vel', b'N\xc3\xa3o biodegrad\xc3\xa1vel')])),
                ('c_pergunta_3', models.CharField(default=b'', max_length=100, verbose_name=b'3. Voc\xc3\xaa tem conhecimento do projeto de Lei que visa a proibi\xc3\xa7\xc3\xa3o da distribui\xc3\xa7\xc3\xa3o das sacolas pl\xc3\xa1sticas pelos estabelecimentos comerciais?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')])),
                ('c_pergunta_4', models.CharField(default=b'', max_length=100, verbose_name=b'4. Se sim, concorda?', choices=[(b'sim', b'Sim'), (b'n\xc3\xa3o', b'N\xc3\xa3o')])),
                ('entrevistadores', models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

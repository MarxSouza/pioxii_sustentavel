# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20151021_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisa',
            name='estado_civil',
            field=models.CharField(max_length=100, choices=[('solteiro(a)', 'Solteiro(a)'), ('casado(a)', 'Casado(a)'), ('separado(a)', 'Separado(a)'), ('viúvo(a)', 'Viúvo(a)')]),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='nacionalidade',
            field=models.CharField(max_length=100, choices=[('brasileiro(a)', 'Brasileiro(a)'), ('brasileiro naturalizado(a)', 'Brasileiro naturalizado(a)'), ('estrangeiro(a)', 'Estrangeiro(a)')]),
        ),
    ]

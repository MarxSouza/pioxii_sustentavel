# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20151021_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesquisa',
            name='cidade_natal',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='cor_favorita',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='time_favorito',
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='estado_civil',
            field=models.CharField(max_length=100, default='solteiro'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='nacionalidade',
            field=models.CharField(max_length=100, default='brasileiro'),
        ),
    ]

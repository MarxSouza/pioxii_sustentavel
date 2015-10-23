# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_squashed_0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesquisa',
            name='cidade_natal',
            field=models.CharField(default='Pio Xii', max_length=100),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='cor_favorita',
            field=models.CharField(default='azul', max_length=100),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='time_favorito',
            field=models.CharField(default='vasco', max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0023_auto_20151120_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesquisa',
            name='entrevistadores',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='escolaridade',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='funcao',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='idade',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='pesquisa',
            name='sexo',
        ),
    ]

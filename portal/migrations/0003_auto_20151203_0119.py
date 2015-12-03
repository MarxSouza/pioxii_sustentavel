# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20151203_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisa',
            name='idade',
            field=models.CharField(max_length=100, default=''),
        ),
    ]

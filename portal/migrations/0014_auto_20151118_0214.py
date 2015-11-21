# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_auto_20151118_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisa',
            name='c_pergunta_1',
            field=models.IntegerField(default=b'', verbose_name=b'1. Quantas sacolas pl\xc3\xa1sticas s\xc3\xa3o compradas em m\xc3\xa9dia e em qual intervalo de tempo dessa compra?'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='idade',
            field=models.IntegerField(default=b''),
        ),
    ]

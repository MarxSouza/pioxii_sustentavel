# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_auto_20151118_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisa',
            name='c_pergunta_1',
            field=models.IntegerField(),
        ),
    ]

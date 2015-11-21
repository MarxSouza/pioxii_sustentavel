# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_remove_pesquisa_idade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesquisa',
            name='c_pergunta_1',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0016_remove_pesquisa_c_pergunta_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesquisa',
            name='entrevistadores',
        ),
    ]

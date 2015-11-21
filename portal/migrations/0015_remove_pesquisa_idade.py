# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_auto_20151118_0214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesquisa',
            name='idade',
        ),
    ]

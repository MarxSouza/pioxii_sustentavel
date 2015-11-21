# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0017_remove_pesquisa_entrevistadores'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesquisa',
            name='entrevistadores',
            field=models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='idade',
            field=models.IntegerField(default=b''),
        ),
    ]

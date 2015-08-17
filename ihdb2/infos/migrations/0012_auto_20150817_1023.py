# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0011_beamer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='info',
            options={'ordering': ('-modified',)},
        ),
        migrations.AddField(
            model_name='info',
            name='outdated',
            field=models.BooleanField(default=False),
        ),
    ]

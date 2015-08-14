# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0009_motdmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='motdmessage',
            name='display',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0006_auto_20150814_1319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='info',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='info',
            old_name='priority',
            new_name='tag',
        ),
    ]

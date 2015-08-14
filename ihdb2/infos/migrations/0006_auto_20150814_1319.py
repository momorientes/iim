# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0005_auto_20150814_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='priority',
            field=models.CharField(choices=[(1, 'foo'), (2, 'bar'), (3, 'baz')], default=1, help_text='Priority from 1 to 10, 10 being highest', max_length=255),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0002_remove_info_info_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='priority',
            field=models.IntegerField(help_text='Priority from 1 to 10, 10 being highest', default=1),
        ),
    ]

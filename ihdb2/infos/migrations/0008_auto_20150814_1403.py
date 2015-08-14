# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0007_auto_20150814_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='linklist',
            name='display_on_dashboard',
            field=models.BooleanField(default=False, help_text='Display this URL on the dashboard'),
        ),
        migrations.AlterField(
            model_name='info',
            name='tag',
            field=models.CharField(default=1, choices=[('1', 'info'), ('2', 'TODO'), ('3', 'general information'), ('4', 'issues'), ('5', 'misc')], max_length=255, help_text='Assign a tag'),
        ),
    ]

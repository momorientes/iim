# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('info_id', models.IntegerField(unique=True, help_text='Information ID')),
                ('priority', models.IntegerField(help_text='Priority from 1 to 10, 10 being highest')),
                ('subject', models.CharField(max_length=1024, help_text='A hinting subject')),
                ('details', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created', 'priority'),
            },
        ),
    ]

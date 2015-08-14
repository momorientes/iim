# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0010_motdmessage_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beamer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('beamer', models.IntegerField(choices=[(1, 'Beamer 1'), (2, 'Beamer 2'), (3, 'Beamer 3')])),
                ('lent_to', models.CharField(max_length=255)),
                ('returned', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

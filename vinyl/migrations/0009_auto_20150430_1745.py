# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0008_auto_20150430_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='url',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Strona WWW', blank=True),
        ),
        migrations.AddField(
            model_name='label',
            name='url',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Strona WWW', blank=True),
        ),
    ]

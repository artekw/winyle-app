# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0007_auto_20150430_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='label',
            name='catalog_number',
        ),
        migrations.AddField(
            model_name='album',
            name='catalog_number',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Numer katalogowy', blank=True),
        ),
    ]

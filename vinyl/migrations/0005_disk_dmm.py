# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0004_auto_20150429_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='disk',
            name='dmm',
            field=models.BooleanField(default=False),
        ),
    ]

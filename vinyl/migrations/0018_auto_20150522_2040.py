# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0017_auto_20150522_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='first_press',
            field=models.BooleanField(default=False, verbose_name=b'Pierwsze wydanie'),
        ),
    ]

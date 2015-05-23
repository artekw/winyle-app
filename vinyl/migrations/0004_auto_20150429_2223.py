# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0003_auto_20150429_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover_condition',
            field=models.CharField(default=b'VG', max_length=15, choices=[(b'M', b'Mint'), (b'NM', b'Near Mint'), (b'VG_PLUS', b'Very Good Plus'), (b'VG', b'Very Good'), (b'G_PLUS', b'Good Plus'), (b'G', b'Good'), (b'P', b'Poor')]),
        ),
        migrations.AlterField(
            model_name='album',
            name='vinyl_condition',
            field=models.CharField(default=b'VG', max_length=15, choices=[(b'M', b'Mint'), (b'NM', b'Near Mint'), (b'VG_PLUS', b'Very Good Plus'), (b'VG', b'Very Good'), (b'G_PLUS', b'Good Plus'), (b'G', b'Good'), (b'P', b'Poor')]),
        ),
    ]

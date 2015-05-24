# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0016_album_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='first_press',
            field=models.BooleanField(default=b'False', verbose_name=b'Pierwsze wydanie'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover_condition',
            field=models.CharField(default=b'VG', max_length=15, verbose_name=b'Stan ok\xc5\x82adki', choices=[(b'M', b'Mint'), (b'NM', b'Near Mint'), (b'EX', b'Excelent'), (b'EX_PLUS', b'Excelent+'), (b'EX_MINUS', b'Excelent-'), (b'VG_PLUS', b'Very Good+'), (b'VG', b'Very Good'), (b'G_PLUS', b'Good+'), (b'G', b'Good'), (b'P', b'Poor')]),
        ),
        migrations.AlterField(
            model_name='album',
            name='vinyl_condition',
            field=models.CharField(default=b'VG', max_length=15, verbose_name=b'Stan no\xc5\x9bnika', choices=[(b'M', b'Mint'), (b'NM', b'Near Mint'), (b'EX', b'Excelent'), (b'EX_PLUS', b'Excelent+'), (b'EX_MINUS', b'Excelent-'), (b'VG_PLUS', b'Very Good+'), (b'VG', b'Very Good'), (b'G_PLUS', b'Good+'), (b'G', b'Good'), (b'P', b'Poor')]),
        ),
    ]

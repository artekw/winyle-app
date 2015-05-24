# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0012_auto_20150430_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(default=b'/media/cover/no_cover.jpg', upload_to=b'cover', null=True, verbose_name=b'Ok\xc5\x82adka', blank=True),
        ),
        migrations.AlterField(
            model_name='disk',
            name='size',
            field=models.CharField(default=12, max_length=4, verbose_name=b'Rozmiar no\xc5\x9bnika', choices=[(b' ', b'Brak'), (b'12', b"12''"), (b'7', b"7''")]),
        ),
        migrations.AlterField(
            model_name='disk',
            name='speed',
            field=models.CharField(default=33, max_length=6, verbose_name=b'Pr\xc4\x99dko\xc5\x9b\xc4\x87', choices=[(b' ', b'Brak'), (b'33', b'33 1/3'), (b'45', b'45')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0018_auto_20150522_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='notes',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Uwagi', blank=True),
        ),
        migrations.AlterField(
            model_name='disk',
            name='size',
            field=models.CharField(default=12, max_length=4, verbose_name=b'Rozmiar no\xc5\x9bnika', choices=[(b' ', b'Brak'), (b'12', b'12'), (b'7', b'7')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0006_auto_20150430_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='disk',
            name='speed',
            field=models.CharField(default=33, max_length=6, verbose_name=b'Pr\xc4\x99dko\xc5\x9b\xc4\x87', choices=[(b'33', b'33 1/3'), (b'45', b'45')]),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(verbose_name=b'Artysta', to='vinyl.Artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='disk',
            field=models.ForeignKey(verbose_name=b'No\xc5\x9bnik', to='vinyl.Disk'),
        ),
        migrations.AlterField(
            model_name='album',
            name='label',
            field=models.ForeignKey(verbose_name=b'Label', to='vinyl.Label'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Artysta'),
        ),
    ]

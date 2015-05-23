# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disk',
            name='cover_condition',
        ),
        migrations.RemoveField(
            model_name='disk',
            name='price',
        ),
        migrations.RemoveField(
            model_name='disk',
            name='vinyl_condition',
        ),
        migrations.RemoveField(
            model_name='label',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='label',
            name='year',
        ),
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(null=True, upload_to=b'cover', blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='cover_condition',
            field=models.CharField(default=b'VG', max_length=100),
        ),
        migrations.AddField(
            model_name='album',
            name='price',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='album',
            name='realease_year',
            field=models.DateField(null=True, verbose_name=b'date released', blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='vinyl_condition',
            field=models.CharField(default=b'VG', max_length=100),
        ),
    ]

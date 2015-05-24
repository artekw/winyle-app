# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0014_auto_20150509_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='discog_url',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Link do Discogs', blank=True),
        ),
    ]

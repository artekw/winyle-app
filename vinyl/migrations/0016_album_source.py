# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0015_album_discog_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='source',
            field=models.CharField(default=b'Allegro', max_length=50, null=True, verbose_name=b'\xc5\xb9r\xc3\xb3d\xc5\x82o zakupu', blank=True),
        ),
    ]

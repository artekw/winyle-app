# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0010_remove_album_realease_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='disk',
            name='format_disk',
            field=models.CharField(default=b'LP', max_length=12, verbose_name=b'Format no\xc5\x9bnika', choices=[(b'CD', b'Compact Disk'), (b'LP', b'Vinyl')]),
        ),
    ]

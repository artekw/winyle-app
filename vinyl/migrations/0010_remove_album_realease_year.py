# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0009_auto_20150430_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='realease_year',
        ),
    ]

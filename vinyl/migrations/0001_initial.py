# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('publish_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vinyl_condition', models.CharField(max_length=100)),
                ('cover_condition', models.CharField(max_length=100)),
                ('size', models.IntegerField(default=12)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('catalog_number', models.CharField(max_length=50)),
                ('cover', models.ImageField(null=True, upload_to=b'cover', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='disk',
            field=models.ForeignKey(to='vinyl.Disk'),
        ),
        migrations.AddField(
            model_name='album',
            name='label',
            field=models.ForeignKey(to='vinyl.Label'),
        ),
    ]

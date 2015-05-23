# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinyl', '0005_disk_dmm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Wykonawca/Zesp\xc3\xb3\xc5\x82')),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='vinyl.Artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(upload_to=b'cover', null=True, verbose_name=b'Ok\xc5\x82adka', blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover_condition',
            field=models.CharField(default=b'VG', max_length=15, verbose_name=b'Stan ok\xc5\x82adki', choices=[(b'M', b'Mint'), (b'NM', b'Near Mint'), (b'VG_PLUS', b'Very Good Plus'), (b'VG', b'Very Good'), (b'G_PLUS', b'Good Plus'), (b'G', b'Good'), (b'P', b'Poor')]),
        ),
        migrations.AlterField(
            model_name='album',
            name='price',
            field=models.DecimalField(default=0, verbose_name=b'Cena', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='album',
            name='publish_date',
            field=models.DateTimeField(verbose_name=b'Data wpisu'),
        ),
        migrations.AlterField(
            model_name='album',
            name='realease_year',
            field=models.DateField(null=True, verbose_name=b'Data wydania', blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'Tytu\xc5\x82 albumu'),
        ),
        migrations.AlterField(
            model_name='album',
            name='vinyl_condition',
            field=models.CharField(default=b'VG', max_length=15, verbose_name=b'Stan no\xc5\x9bnika', choices=[(b'M', b'Mint'), (b'NM', b'Near Mint'), (b'VG_PLUS', b'Very Good Plus'), (b'VG', b'Very Good'), (b'G_PLUS', b'Good Plus'), (b'G', b'Good'), (b'P', b'Poor')]),
        ),
        migrations.AlterField(
            model_name='disk',
            name='dmm',
            field=models.BooleanField(default=False, verbose_name=b'Digital Metal Mastering'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='size',
            field=models.CharField(default=12, max_length=4, verbose_name=b'Rozmiar no\xc5\x9bnika', choices=[(b'12', b"12''"), (b'7', b"7''")]),
        ),
        migrations.AlterField(
            model_name='label',
            name='catalog_number',
            field=models.CharField(max_length=50, verbose_name=b'Numer katalogowy'),
        ),
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'Wydawca'),
        ),
    ]

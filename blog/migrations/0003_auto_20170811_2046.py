# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170810_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='album_artist',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='album_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='album_art',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

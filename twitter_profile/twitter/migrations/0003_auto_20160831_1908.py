# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-31 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20160831_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

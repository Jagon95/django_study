# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20161102_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]

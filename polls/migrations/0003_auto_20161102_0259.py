# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-01 23:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20161102_0242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choise_text',
            new_name='choice_text',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-29 17:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20160529_1626'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoinifyCallback',
            new_name='CoinifyAPICallback',
        ),
    ]

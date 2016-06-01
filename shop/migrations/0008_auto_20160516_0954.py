# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 09:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20160515_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproductrelation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 16, 9, 53, 59, 584701, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderproductrelation',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 5, 16, 9, 54, 3, 23885, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
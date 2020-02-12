# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-25 13:45
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("camps", "0025_auto_20180318_1250"),
        ("teams", "0025_auto_20180318_1318"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="camp",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="teams",
                to="camps.Camp",
            ),
        )
    ]

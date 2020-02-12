# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 13:39


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("camps", "0017_remove_camp_description"),
        ("program", "0013_auto_20170121_1312"),
    ]

    operations = [
        migrations.AddField(
            model_name="speaker",
            name="camp",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="speakers",
                to="camps.Camp",
            ),
        )
    ]

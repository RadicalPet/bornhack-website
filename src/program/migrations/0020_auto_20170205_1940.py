# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 18:40
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("program", "0019_auto_20170205_1940")]

    operations = [
        migrations.AlterField(
            model_name="eventinstance",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="eventinstances",
                to="program.EventLocation",
            ),
        )
    ]

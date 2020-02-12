# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-22 21:04
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("teams", "0017_auto_20171122_1928")]

    operations = [
        migrations.AlterField(
            model_name="teamtask",
            name="team",
            field=models.ForeignKey(
                help_text="The team this task belongs to",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="teams.Team",
            ),
        )
    ]

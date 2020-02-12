# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 18:40
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("camps", "0019_auto_20170131_1849"),
        ("program", "0018_eventtype_notifications"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventLocation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField()),
                ("icon", models.URLField()),
                (
                    "camp",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="eventlocations",
                        to="camps.Camp",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="eventinstance",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="eventinstances",
                to="program.EventLocation",
            ),
        ),
    ]

# Generated by Django 2.0.4 on 2018-05-21 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("program", "0054_auto_20180520_1509")]

    operations = [
        migrations.CreateModel(
            name="Url",
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
                ("url", models.URLField(help_text="The actual URL")),
                (
                    "event",
                    models.ForeignKey(
                        blank=True,
                        help_text="The event proposal object this URL belongs to",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="urls",
                        to="program.Event",
                    ),
                ),
                (
                    "eventproposal",
                    models.ForeignKey(
                        blank=True,
                        help_text="The event proposal object this URL belongs to",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="urls",
                        to="program.EventProposal",
                    ),
                ),
                (
                    "speaker",
                    models.ForeignKey(
                        blank=True,
                        help_text="The speaker proposal object this URL belongs to",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="urls",
                        to="program.Speaker",
                    ),
                ),
                (
                    "speakerproposal",
                    models.ForeignKey(
                        blank=True,
                        help_text="The speaker proposal object this URL belongs to",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="urls",
                        to="program.SpeakerProposal",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="UrlType",
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
                (
                    "name",
                    models.CharField(help_text="The name of this type", max_length=25),
                ),
                (
                    "icon",
                    models.CharField(
                        help_text="Name of the fontawesome icon to use without the 'fa-' part",
                        max_length=100,
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="url",
            name="urltype",
            field=models.ForeignKey(
                help_text="The type of this URL",
                on_delete=django.db.models.deletion.PROTECT,
                to="program.UrlType",
            ),
        ),
    ]

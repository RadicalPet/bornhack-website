# Generated by Django 2.0.4 on 2018-06-03 12:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("program", "0059_auto_20180523_2241")]

    operations = [
        migrations.AlterField(
            model_name="eventtrack",
            name="camp",
            field=models.ForeignKey(
                help_text="The Camp this Track belongs to",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="eventtracks",
                to="camps.Camp",
            ),
        ),
        migrations.AlterField(
            model_name="eventtrack",
            name="managers",
            field=models.ManyToManyField(
                blank=True,
                help_text="If this track is managed by someone other than the Content team pick the users here.",
                related_name="managed_tracks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="eventtrack",
            name="name",
            field=models.CharField(help_text="The name of this Track", max_length=100),
        ),
        migrations.AlterField(
            model_name="eventtrack",
            name="slug",
            field=models.SlugField(help_text="The url slug for this Track"),
        ),
        migrations.AlterField(
            model_name="speakerproposal",
            name="camp",
            field=models.ForeignKey(
                editable=False,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="speakerproposals",
                to="camps.Camp",
            ),
        ),
    ]

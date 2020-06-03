# Generated by Django 3.0.3 on 2020-04-21 20:54

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0003_taggeditem_add_unique_index"),
        ("program", "0089_event_conflicts_blank"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]

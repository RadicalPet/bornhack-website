# Generated by Django 2.2.3 on 2019-07-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0011_save_badge_token_to_db"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discountticket",
            name="badge_token",
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name="shopticket",
            name="badge_token",
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name="sponsorticket",
            name="badge_token",
            field=models.CharField(max_length=64),
        ),
    ]

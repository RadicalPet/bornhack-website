# Generated by Django 2.1.7 on 2019-07-13 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0007_ride_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='author',
            field=models.CharField(default='Anonymous', help_text='Let people know who posted this', max_length=100),
        ),
    ]

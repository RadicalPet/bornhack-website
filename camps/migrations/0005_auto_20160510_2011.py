# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0004_camp_ticket_sale_open'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camp',
            name='ticket_sale_open',
        ),
        migrations.AddField(
            model_name='camp',
            name='shop_open',
            field=models.BooleanField(default=False, help_text='Whether the shop is open or not.', verbose_name='Shop open?'),
        ),
    ]

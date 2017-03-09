# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0034_auto_20170131_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_comment',
            field=models.TextField(blank=True, default='', help_text='If you have any comments about the order please enter them here.', verbose_name='Customer comment'),
        ),
    ]
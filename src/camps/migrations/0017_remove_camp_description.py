# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 21:59


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("camps", "0016_camp_description")]

    operations = [migrations.RemoveField(model_name="camp", name="description")]

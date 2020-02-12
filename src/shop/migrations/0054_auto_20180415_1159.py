# Generated by Django 2.0.4 on 2018-04-15 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("shop", "0053_auto_20180318_0906")]

    operations = [
        migrations.AddField(
            model_name="product",
            name="stock_amount",
            field=models.IntegerField(
                blank=True,
                help_text="Initial amount available in stock if there is a limited supply, e.g. fridge space",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="epaypayment",
            name="order",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT, to="shop.Order"
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="customorder",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="shop.CustomOrder",
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="order",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="shop.Order",
            ),
        ),
    ]

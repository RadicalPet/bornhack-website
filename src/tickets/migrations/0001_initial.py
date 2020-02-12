# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-19 20:21
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("camps", "0022_camp_colour"),
        ("sponsors", "0006_auto_20170715_1110"),
        ("shop", "0047_auto_20170522_1942"),
    ]

    operations = [
        migrations.CreateModel(
            name="DiscountTicket",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("qrcode_base64", models.TextField(blank=True, null=True)),
                ("checked_in", models.BooleanField(default=False)),
                (
                    "price",
                    models.IntegerField(
                        help_text="Price of the discounted ticket (in DKK, including VAT)."
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="ShopTicket",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("qrcode_base64", models.TextField(blank=True, null=True)),
                ("checked_in", models.BooleanField(default=False)),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Name of the person this ticket belongs to. This can be different from the buying user.",
                        max_length=100,
                        null=True,
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shoptickets",
                        to="shop.Order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.Product"
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="SponsorTicket",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("qrcode_base64", models.TextField(blank=True, null=True)),
                ("checked_in", models.BooleanField(default=False)),
                (
                    "sponsor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sponsors.Sponsor",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="TicketType",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.TextField()),
                (
                    "camp",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="camps.Camp",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="sponsorticket",
            name="ticket_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tickets.TicketType",
            ),
        ),
        migrations.AddField(
            model_name="shopticket",
            name="ticket_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tickets.TicketType",
            ),
        ),
        migrations.AddField(
            model_name="discountticket",
            name="ticket_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tickets.TicketType",
            ),
        ),
    ]

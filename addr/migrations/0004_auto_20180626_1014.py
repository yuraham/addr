# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 01:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('addr', '0003_auto_20180626_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='save_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 26, 1, 14, 28, 309482, tzinfo=utc)),
        ),
    ]
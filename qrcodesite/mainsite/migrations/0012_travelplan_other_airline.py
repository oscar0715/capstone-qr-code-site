# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0011_auto_20170401_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelplan',
            name='other_airline',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

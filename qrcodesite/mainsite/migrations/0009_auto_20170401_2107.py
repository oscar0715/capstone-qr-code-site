# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0008_auto_20170401_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelplan',
            name='other_purpose',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

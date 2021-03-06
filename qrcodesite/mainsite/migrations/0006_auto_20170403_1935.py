# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20170403_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='airportactivity',
            name='other_service',
            field=models.CharField(blank=True, max_length=300, verbose_name='Other than the places listed above, what other services would you like to have at the airport?'),
        ),
        migrations.AlterField(
            model_name='airportactivity',
            name='why_not',
            field=models.CharField(blank=True, choices=[('A', 'Shops far from waiting area'), ('B', 'Shops are not appealing'), ('C', 'Do not have enough time'), ('D', 'Prefer to be at my gate'), ('E', 'Too expensive'), ('F', 'Other')], max_length=1, verbose_name='If you did not visit any of these areas, why not?'),
        ),
    ]

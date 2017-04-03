# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20170403_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='airportactivity',
            name='other_why_not',
            field=models.CharField(blank=True, max_length=200, verbose_name='If you choose "other" in the places you have visited, please specify'),
        ),
        migrations.AddField(
            model_name='airportactivity',
            name='why_not',
            field=models.CharField(blank=True, choices=[('A', 'Shops far from waiting area'), ('B', 'Shops are not appealing'), ('C', 'Do not have enough time'), ('D', 'Prefer to be at my gate'), ('E', 'Too expensive'), ('F', 'Other')], default='Unspecified', max_length=1, verbose_name='If you did not visit any of these areas, why not?'),
        ),
    ]
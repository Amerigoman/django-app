# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='img_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]

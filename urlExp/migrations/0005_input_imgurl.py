# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlExp', '0004_auto_20160811_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='imgUrl',
            field=models.CharField(default='', max_length=200),
        ),
    ]

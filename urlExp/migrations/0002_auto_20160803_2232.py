# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlExp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='destination',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='input',
            name='status',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='input',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]

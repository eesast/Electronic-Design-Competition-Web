# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-21 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0020_auto_20161021_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfile',
            name='permissions',
            field=models.CharField(choices=[('2', '登陆可见'), ('1', '公开')], max_length=1),
        ),
    ]

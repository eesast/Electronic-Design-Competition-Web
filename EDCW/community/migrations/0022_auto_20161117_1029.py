# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-17 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0021_auto_20161021_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfile',
            name='permissions',
            field=models.CharField(choices=[('1', '公开'), ('2', '登陆可见')], max_length=1),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_auto_20160918_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfile',
            name='permissions',
            field=models.CharField(choices=[('1', '公开'), ('2', '登陆可见')], max_length=1),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0016_auto_20160925_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfile',
            name='permissions',
            field=models.CharField(choices=[('2', '登陆可见'), ('1', '公开')], max_length=1),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20160923_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(default='head_images/custom.png', upload_to='head_images'),
        ),
    ]

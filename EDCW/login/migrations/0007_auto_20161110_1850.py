# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-10 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_merge_20161021_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(default='head_images\\custom.png', upload_to='head_images'),
        ),
    ]
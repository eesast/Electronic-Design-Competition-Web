# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='file_attached',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
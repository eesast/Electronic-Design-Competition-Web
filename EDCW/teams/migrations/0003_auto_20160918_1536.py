# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 07:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='leader',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lead', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(related_name='in_team', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
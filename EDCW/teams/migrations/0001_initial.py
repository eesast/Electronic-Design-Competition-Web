# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 05:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('student_id', models.CharField(max_length=20)),
                ('is_leader', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('intro', models.CharField(max_length=50)),
                ('is_full', models.BooleanField(default=False)),
                ('leader', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lead', to='teams.Member')),
                ('members', models.ManyToManyField(related_name='in_team', to='teams.Member')),
            ],
        ),
    ]
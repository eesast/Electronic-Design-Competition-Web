# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 12:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0002_auto_20160911_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_content',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='replier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postfile',
            name='permissions',
            field=models.CharField(choices=[('1', '公开'), ('2', '登陆可见')], max_length=1),
        ),
    ]

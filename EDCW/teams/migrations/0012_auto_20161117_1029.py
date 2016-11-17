# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-17 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0011_auto_20161110_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='fuhuo_time',
            field=models.IntegerField(blank=True, choices=[(-1, 'None')], default=-1, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='other_fuhuo_time',
            field=models.CharField(blank=True, default=0, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='first_time',
            field=models.IntegerField(choices=[(-1, 'None'), (0, '12日09:30---09:36'), (1, '12日09:36---09:42'), (2, '12日09:42---09:48'), (3, '12日09:48---09:54'), (4, '12日09:54---10:00'), (5, '12日10:00---10:06'), (6, '12日10:06---10:12'), (7, '12日10:12---10:18'), (8, '12日10:18---10:24'), (9, '12日10:24---10:30'), (10, '12日10:30---10:36'), (11, '12日10:36---10:42'), (12, '12日10:42---10:48'), (13, '12日10:48---10:54'), (14, '12日10:54---11:00'), (15, '12日11:00---11:06'), (16, '12日11:06---11:12'), (17, '12日11:12---11:18'), (18, '12日11:18---11:24'), (19, '12日11:24---11:30'), (20, '12日13:30---13:36'), (21, '12日13:36---13:42'), (22, '12日13:42---13:48'), (23, '12日13:48---13:54'), (24, '12日13:54---14:00'), (25, '12日14:00---14:06'), (26, '12日14:06---14:12'), (27, '12日14:12---14:18'), (28, '12日14:18---14:24'), (29, '12日14:24---14:30'), (30, '12日14:30---14:36'), (31, '12日14:36---14:42'), (32, '12日14:42---14:48'), (33, '12日14:48---14:54'), (34, '12日14:54---15:00'), (35, '12日15:00---15:06'), (36, '12日15:06---15:12'), (37, '12日15:12---15:18'), (38, '12日15:18---15:24'), (39, '12日15:24---15:30'), (40, '12日15:30---15:36'), (41, '12日15:36---15:42'), (42, '12日15:42---15:48'), (43, '12日15:48---15:54'), (44, '12日15:54---16:00'), (45, '12日16:00---16:06'), (46, '12日16:06---16:12'), (47, '12日16:12---16:18'), (48, '12日16:18---16:24'), (49, '12日16:24---16:30'), (50, '12日16:30---16:36'), (51, '12日16:36---16:42'), (52, '12日16:42---16:48'), (53, '12日16:48---16:54'), (54, '12日16:54---17:00'), (55, '13日09:30---09:36'), (56, '13日09:36---09:42'), (57, '13日09:42---09:48'), (58, '13日09:48---09:54'), (59, '13日09:54---10:00'), (60, '13日10:00---10:06'), (61, '13日10:06---10:12'), (62, '13日10:12---10:18'), (63, '13日10:18---10:24'), (64, '13日10:24---10:30'), (65, '13日10:30---10:36'), (66, '13日10:36---10:42'), (67, '13日10:42---10:48'), (68, '13日10:48---10:54'), (69, '13日10:54---11:00'), (70, '13日11:00---11:06'), (71, '13日11:06---11:12'), (72, '13日11:12---11:18'), (73, '13日11:18---11:24'), (74, '13日11:24---11:30'), (75, '13日13:30---13:36'), (76, '13日13:36---13:42'), (77, '13日13:42---13:48'), (78, '13日13:48---13:54'), (79, '13日13:54---14:00'), (80, '13日14:00---14:06'), (81, '13日14:06---14:12'), (82, '13日14:12---14:18'), (83, '13日14:18---14:24'), (84, '13日14:24---14:30'), (85, '13日14:30---14:36'), (86, '13日14:36---14:42'), (87, '13日14:42---14:48'), (88, '13日14:48---14:54'), (89, '13日14:54---15:00'), (90, '13日15:00---15:06'), (91, '13日15:06---15:12'), (92, '13日15:12---15:18'), (93, '13日15:18---15:24'), (94, '13日15:24---15:30'), (95, '13日15:30---15:36'), (96, '13日15:36---15:42'), (97, '13日15:42---15:48'), (98, '13日15:48---15:54'), (99, '13日15:54---16:00'), (100, '13日16:00---16:06'), (101, '13日16:06---16:12'), (102, '13日16:12---16:18'), (103, '13日16:18---16:24'), (104, '13日16:24---16:30'), (105, '13日16:30---16:36'), (106, '13日16:36---16:42'), (107, '13日16:42---16:48'), (108, '13日16:48---16:54'), (109, '13日16:54---17:00')], default=-1),
        ),
        migrations.AlterField(
            model_name='team',
            name='pre_time',
            field=models.IntegerField(choices=[(-1, 'None'), (0, '12日09:30---09:36'), (1, '12日09:36---09:42'), (2, '12日09:42---09:48'), (3, '12日09:48---09:54'), (4, '12日09:54---10:00'), (5, '12日10:00---10:06'), (6, '12日10:06---10:12'), (7, '12日10:12---10:18'), (8, '12日10:18---10:24'), (9, '12日10:24---10:30'), (10, '12日10:30---10:36'), (11, '12日10:36---10:42'), (12, '12日10:42---10:48'), (13, '12日10:48---10:54'), (14, '12日10:54---11:00'), (15, '12日11:00---11:06'), (16, '12日11:06---11:12'), (17, '12日11:12---11:18'), (18, '12日11:18---11:24'), (19, '12日11:24---11:30'), (20, '12日13:30---13:36'), (21, '12日13:36---13:42'), (22, '12日13:42---13:48'), (23, '12日13:48---13:54'), (24, '12日13:54---14:00'), (25, '12日14:00---14:06'), (26, '12日14:06---14:12'), (27, '12日14:12---14:18'), (28, '12日14:18---14:24'), (29, '12日14:24---14:30'), (30, '12日14:30---14:36'), (31, '12日14:36---14:42'), (32, '12日14:42---14:48'), (33, '12日14:48---14:54'), (34, '12日14:54---15:00'), (35, '12日15:00---15:06'), (36, '12日15:06---15:12'), (37, '12日15:12---15:18'), (38, '12日15:18---15:24'), (39, '12日15:24---15:30'), (40, '12日15:30---15:36'), (41, '12日15:36---15:42'), (42, '12日15:42---15:48'), (43, '12日15:48---15:54'), (44, '12日15:54---16:00'), (45, '12日16:00---16:06'), (46, '12日16:06---16:12'), (47, '12日16:12---16:18'), (48, '12日16:18---16:24'), (49, '12日16:24---16:30'), (50, '12日16:30---16:36'), (51, '12日16:36---16:42'), (52, '12日16:42---16:48'), (53, '12日16:48---16:54'), (54, '12日16:54---17:00')], default=-1),
        ),
    ]
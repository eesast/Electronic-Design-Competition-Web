# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=20)
    leader = models.CharField(max_length=10)


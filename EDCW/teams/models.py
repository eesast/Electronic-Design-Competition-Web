# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.apps import AppConfig
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=10)
    student_id = models.CharField(max_length=20)
    is_leader = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=20)
    intro = models.CharField(max_length=50)
    leader = models.OneToOneField('Member', on_delete=models.CASCADE, related_name='lead')
    members = models.ManyToManyField('Member', related_name='in_team')
    is_full = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' -- ' + self.leader

class Application(models.Model):
    applicant = models.ForeignKey('Member', on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)

    def __str__(self):
        return self.applicant.name + ' --> ' + self.team.name


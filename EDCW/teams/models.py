# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    DSP = 'D'
    MCU = 'M'
    FPGA = 'F'
    GROUP_CHOICES = (
        (DSP, 'DSP'),
        (MCU, '单片机'),
        (FPGA, 'FPGA'),
    )
    group = models.CharField(
        max_length=1,
        choices=GROUP_CHOICES,
        default='M',
    )
    name = models.CharField(max_length=20)
    intro = models.CharField(max_length=50)
    leader = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leads')
    members = models.ManyToManyField(User, related_name='in_team')
    is_full = models.BooleanField(default=False)


    def __str__(self):
        return self.name + ' -- ' + self.leader.username

class Application(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)

    def __str__(self):
        return self.applicant.username + ' --> ' + self.team.name


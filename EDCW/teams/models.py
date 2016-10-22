# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime

timelist = [datetime.datetime(101, 1, 1, hour=9, minute=30)
            + i*datetime.timedelta(minutes=6) for i in range(20)]
timelist = timelist + [datetime.datetime(101, 1, 1, hour=13, minute=30)
                      + i*datetime.timedelta(minutes=6) for i in range(35)]
pre = zip(range(len(timelist)),
          [p.strftime("%H:%M")+'---'+(p+datetime.timedelta(minutes=6)).strftime("%H:%M") for p in timelist])
pre_time_choice = [(-1, 'None') ] + [p for p in pre]

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
    pre_time = models.IntegerField(choices = pre_time_choice, default=-1)
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




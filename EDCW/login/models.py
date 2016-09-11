from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.db import models

@python_2_unicode_compatible
class Team(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name



@python_2_unicode_compatible
class Member(models.Model):
    team = models.ForeignKey(Team,null=True,blank=True,on_delete=models.SET_NULL)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    def __str__(self):
        return self.name

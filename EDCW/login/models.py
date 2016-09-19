from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.conf import settings

#@python_2_unicode_compatible
#class Team(models.Model):
#	name =  models.CharField(max_length=20)
#	def __str__(self):
#		return self.name





@python_2_unicode_compatible
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile' )
    student_id = models.CharField(max_length=20, blank=True)
    is_leader = models.BooleanField(default=False)
    image = models.ImageField(upload_to='head_images',default='head_images/default.png')
    def __str__(self):
        return self.user.username


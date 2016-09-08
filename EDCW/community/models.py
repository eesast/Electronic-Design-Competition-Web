from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django import forms


class Post(models.Model):
    title = models.CharField(u'评论标题',max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    content = models.TextField(u'内容',blank=True, null=True)
    sender = models.CharField(max_length=30)
    replycount = models.IntegerField(default=0)
    summary = models.CharField(u'摘要',blank=True, null=True,max_length=100)
    head_img = models.ImageField(upload_to="uploads",null=True)
    category = models.ForeignKey("Category",verbose_name='版块名称',null=True)
    priority = models.IntegerField(default=1000,verbose_name="优先级")
    def __unicode__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey("UserProfile")
    comment_content= models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey("self",related_name='p_comment',blank=True,null=True)

    def __unicode__(self):
        return self.user

	
	
class Category(models.Model):
    name = models.CharField(max_length=64,unique=True,verbose_name="板块名称")
    def __unicode__(self):
        return self.name	

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    groups = models.ManyToManyField("UserGroup")
    def __unicode__(self):
        return self.name

class UserGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)
    def __unicode__(self):
        return self.name


	
		
		
		
		
		
# Create your models here.

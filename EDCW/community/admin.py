from django.contrib import admin
from community import models
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','sender','timestamp','replycount','category')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','replier','content','replytime')

admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Comment,CommentAdmin)


# Register your models here.

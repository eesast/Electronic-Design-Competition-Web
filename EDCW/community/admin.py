from django.contrib import admin
from community import models
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','sender','timestamp','replycount')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','date')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Comment,CommentAdmin)


# Register your models here.

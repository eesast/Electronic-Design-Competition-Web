from django.contrib import admin
from community import models
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','sender','timestamp','replycount','category')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','replytime')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Comment,CommentAdmin)


# Register your models here.

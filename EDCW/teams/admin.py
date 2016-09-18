from django.contrib import admin
from teams import models

class TeamAdmin(admin.ModelAdmin):
    model = models.Team
    filter_horizontal = ('members', )

admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.Application)

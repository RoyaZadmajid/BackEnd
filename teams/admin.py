from django.contrib import admin

from .models import Team, TeamStatic


class TeamAdmin(admin.ModelAdmin):
    fields = (
        'name',
    )


class TeamStaticAdmin(admin.ModelAdmin):
    fields = (
        'team',
        'date_reported',
        'happiness_num_users',
        'average_happiness',
    )


admin.site.register(Team, TeamAdmin)
admin.site.register(TeamStatic, TeamStaticAdmin)

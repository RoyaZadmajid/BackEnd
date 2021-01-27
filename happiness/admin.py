from django.contrib import admin

from .models import TeamMember, TeamMemberHappiness
from .forms import TeamMemberHappinessForm


class TeamMemberAdmin(admin.ModelAdmin):
    fields = (
        'team_member',
        'team',
    )


class TeamMemberHappinessAdmin(admin.ModelAdmin):
    form = TeamMemberHappinessForm


admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(TeamMemberHappiness, TeamMemberHappinessAdmin)

import json
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from model_utils.models import TimeStampedModel

from teams.models import Team, TeamStatic


class TeamMember(models.Model):
    team_member = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.team_member)


class TeamMemberHappiness(TimeStampedModel):
    HAPPINESS_UNHAPPY = 1
    HAPPINESS_NOT_VERY_HAPPY = 2
    HAPPINESS_NEITHER_HAPPY_NOR_UNHAPPY = 3
    HAPPINESS_HAPPY = 4
    HAPPINESS_VERY_HAPPY = 5

    HAPPINESS_LEVEL = (
        ('Unhappy', 'Unhappy'),
        ('Not Very Happy', 'Not Very Happy'),
        ('Neither Happy Nor Unhappy', 'Neither Happy Nor Unhappy'),
        ('Happy', 'Happy'),
        ('Very Happy', 'Very Happy'),
    )

    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    date_reported = models.DateField()
    happiness_level = models.CharField(max_length=255, choices=HAPPINESS_LEVEL, default=HAPPINESS_VERY_HAPPY,
                                       db_index=True)

    def __str__(self):
        components = [str(self.team_member), str(self.date_reported)]
        return ' | '.join(components)


def happiness_statics_receiver(sender, instance, created, **kwargs):
    """
    happiness_statics_receiver method is a receiver that gets to create a TeamStatic instance as soon as a new
    TeamMemberHappiness instance is saved.
    """
    if created:
        team = instance.team_member.team
        reporting_day = instance.date_reported
        team_member_mood = instance.happiness_level
        team_static_obj = TeamStatic.objects.filter(team=team, date_reported=reporting_day).first()
        if not team_static_obj:
            user_num_at_happiness_levels = {
                'Unhappy': 0,
                'Not Very Happy': 0,
                'Neither Happy Nor Unhappy': 0,
                'Happy': 0,
                'Very Happy': 0,
            }
            user_num_at_happiness_levels[team_member_mood] += 1
            TeamStatic.objects.create(team=team, date_reported=reporting_day,
                                      happiness_num_users=user_num_at_happiness_levels)
        else:
            json_acceptable_string = team_static_obj.happiness_num_users.replace("'", "\"")
            d = json.loads(json_acceptable_string)
            d[team_member_mood] += 1
            team_static_obj.happiness_num_users = d
            team_static_obj.save()


post_save.connect(happiness_statics_receiver, sender=TeamMemberHappiness)



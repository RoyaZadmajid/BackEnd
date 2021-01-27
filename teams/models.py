import simplejson

from decimal import Decimal
from django.db import models
from model_utils.models import TimeStampedModel


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TeamStatic(TimeStampedModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_reported = models.DateField()
    happiness_num_users = models.TextField(verbose_name='# of Users of a Happiness Level', blank=True)
    average_happiness = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))

    @property
    def props_dict(self):
        return simplejson.loads(self.happiness_num_users)

    def __str__(self):
        components = [str(self.team), str(self.date_reported)]
        return ' | '.join(components)

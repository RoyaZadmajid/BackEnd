from django.test import TestCase
from django.utils import timezone

from .models import Team, TeamStatic


# this class is to test Team Model Creation
class TestTeamModel(TestCase):

    def create_team_instance(self):
        return Team.objects.create(name='test_team')

    def test_team_creation(self):
        team_instance = self.create_team_instance()
        self.assertTrue(isinstance(team_instance, Team))
        self.assertEqual(team_instance.__unicode__(), team_instance.name)


# this class is to test TeamStatic Model Creation
class TestTeamStaticModel(TestCase):

    def create_team_static_instance(self):
        return TeamStatic.objects.create(team="Engineering", date_reported=timezone.now(),
                                         happiness_num_users={'Happy': 2, }, average_happiness='2.10')

    def test_teamstatic_creation(self):
        team_static_instance = self.create_team_static_instance()
        self.assertTrue(isinstance(team_static_instance, TeamStatic))
        self.assertEqual(team_static_instance.__unicode__(), team_static_instance.team)

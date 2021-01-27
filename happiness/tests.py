from django.test import TestCase

from .models import TeamMember, TeamMemberHappiness


def test(request):
    print("99999999999999999999")
    all_team_members = TeamMember.objects.all()
    print("AAAAAAAAAAAA: ", all_team_members)
    TeamMemberHappiness.objects.create(team_member=all_team_members.first(), date_reported="2021-01-27",
                                       happiness_level=2)

    # team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    # date_reported = models.DateField()
    # happiness_level = models.PositiveIntegerField(choices=HAPPINESS_LEVEL, default=HAPPINESS_VERY_HAPPY, db_index=True)


# this class is to test TeamMember Model Creation
class TestTeamMemberModel(TestCase):

    def create_team_instance(self):
        return TeamMember.objects.create(team_member='test_name', team='Engineering')

    def test_team_creation(self):
        team_member_instance = self.create_team_instance()
        self.assertTrue(isinstance(team_member_instance, TeamMember))
        self.assertEqual(team_member_instance.__unicode__(), team_member_instance.team_member)

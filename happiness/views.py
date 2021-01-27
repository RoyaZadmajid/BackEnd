from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.utils.api_exceptions import APIError
from .permissions import IsAdminStaff

from .models import TeamMember
from teams.models import TeamStatic


class TeamHappinessStatics(APIView):
    http_method_names = ['get', 'head', 'options']
    serializer_class = None
    permission_classes = [IsAuthenticated, IsAdminStaff]

    def get(self, request):
        if request.user is None:
            statics_of_team_objects = TeamStatic.objects.all()

            return statics_of_team_objects.average_happiness

        elif request.user.is_authenticated or request.user.is_superuser or request.user.is_staff:
            user = TeamMember.objects.filter(team_member=request.user).first()

            if user:
                user_team = user.team
                static_of_user_team = TeamStatic.objects.filter(team=user_team,
                                                                date_reported=datetime.today().strftime(
                                                                    '%Y-%m-%d')).first()

                if static_of_user_team:

                    data = {
                        'number of team members at each happiness level': static_of_user_team.happiness_num_users,
                        'team_average_happiness': static_of_user_team.average_happiness,
                    }
                    return Response(data)
                else:
                    raise APIError(error='Team Static not Found')

            else:
                raise APIError(error='User not Found')

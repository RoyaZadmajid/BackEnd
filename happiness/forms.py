from django import forms

from .models import TeamMemberHappiness


class TeamMemberHappinessForm(forms.ModelForm):
    class Meta:
        model = TeamMemberHappiness
        exclude = ('',)

    def clean(self):
        team_member = self.cleaned_data.get('team_member')
        date_reported = self.cleaned_data.get('date_reported')
        member_happiness_query = TeamMemberHappiness.objects.filter(team_member=team_member,
                                                                    date_reported=date_reported)

        if member_happiness_query.exists():
            raise forms.ValidationError(
                'The Happiness Level can not be submitted more than once a day by a Team Member.')

        return self.cleaned_data

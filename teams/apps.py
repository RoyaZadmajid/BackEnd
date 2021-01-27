from django.apps import AppConfig
# from django.db.models.signals import post_save
#
# from happiness.models import TeamMemberHappiness
# from .signals import happiness_statics_reciever


class TeamsConfig(AppConfig):
    name = 'teams'

    # def ready(self):
    #     import teams.signals
    #
    # def ready(self):
    #     print("THISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    #     post_save.connect(happiness_statics_reciever, sender=TeamMemberHappiness)

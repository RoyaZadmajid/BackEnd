from django.db.models.signals import post_save
from django.dispatch import receiver

from happiness.models import TeamMemberHappiness


@receiver(post_save, sender=TeamMemberHappiness)
def happiness_statics_reciever(sender, instance, created, **kwargs):
    pass

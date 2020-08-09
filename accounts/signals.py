from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.model import User
from accounts.models import User_Account, Profile


@receiver(post_save, sender=User_Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_name = str(instance.email).split("@")[0]
        Profile.objects.create(
            user=instance,
            name=user_name
        )

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_user_profile_receiver (sender, instance, created, **kwargs):
    print(created)
    if created:
        print('Profile Created')
        UserProfile.objects.create(user=instance)
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            UserProfile.objects.create(user=instance)
        print('Updated')
@receiver(pre_save, sender=User)        
def pre_save_user_profile_receiver(sender, instance, *args, **kwargs):
    print(instance.username,'pre_save_user_profile_receiver')
    print(instance.email,'pre_save_user_profile_receiver')
    
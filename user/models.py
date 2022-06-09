from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

#
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  home_address =models.CharField(max_length=250, blank=True, default="-")
  phone_number =  models.CharField(max_length=250, blank=True, default="-")
  latitude = models.CharField(max_length=250, blank=True, default="-")
  longitude = models.CharField(max_length=250, blank=True, default="-")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()

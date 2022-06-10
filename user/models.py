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


# Model to store login/logout activities
class LoginLogoutActivities(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  login_time = models.DateTimeField(auto_now_add=True)
  logout_time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"User: {self.user.username}, Logged in at: {str(self.login_time)[:16]}, Logged out at: {str(self.logout_time)[:16]}"

from django.dispatch import receiver
from django.contrib.auth.signals import (
  user_logged_in,
  user_logged_out,
)
from django.contrib.auth.models import User
from user.models import LoginLogoutActivities

# Track login activities
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
  print('user has logged in')
  log_user = LoginLogoutActivities()
  log_user.user = User.objects.get(pk=user.id)
  log_user.save()


# Track user logg out
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
  print('user has logged out')
  log_user = LoginLogoutActivities()
  log_user.user = User.objects.get(pk=user.id)
  log_user.save()

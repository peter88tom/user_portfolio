from django.contrib import admin
from user.models import Profile, LoginLogoutActivities

# Register your models here.
admin.site.register(Profile)
admin.site.register(LoginLogoutActivities)

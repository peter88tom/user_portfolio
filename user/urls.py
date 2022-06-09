from django.urls import path
from user import views


urlpatterns = [
    path('', views.login_index, name="login"),
    path('user/profile', views.user_profile, name="user-profile"),
]

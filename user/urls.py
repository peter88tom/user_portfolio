from django.urls import path
from django.contrib.auth import views as auth_views
from user import views


urlpatterns = [
    path('', views.login_index, name="login"),
    path('user/profile', views.user_profile, name="user-profile"),
    path('user/logout', auth_views.LogoutView.as_view(), {'next_page':'login'}, name="logout"),
    path('user/signup', views.signup, name="signup"),
]

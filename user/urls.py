from django.urls import path
from user import views


urlpatterns = [
    path('', views.login_index, name="index")
]

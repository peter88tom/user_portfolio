from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import  User
from user.models import Profile



# Default page for the application
def login_index(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    # check if authentication is successfully
    if user is not None and user.is_active:

      # create user session
      login(request, user)

      # redirect user to profile page
      return redirect('user-profile')

    else:
      # authentication failed, redirect user back to login page
      messages.warning(request, 'Wrong username or password')
      return redirect('login')

  return render(request, 'login.html')


"""
 page where user will be redirected after login
 user will be able to update their profile info
"""
def user_profile(request):
  if request.method == 'POST':
    # update user profile
    user = User.objects.get(pk=request.user.id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.profile.home_address = request.POST['home_address']
    user.profile.phone_number = request.POST['phone_number']

    user.save()

    # redirect back to their profile
    messages.success(request, 'Profile updated successfully')
    return redirect('user-profile')

  return render(request, 'profile.html')

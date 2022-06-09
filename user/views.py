from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


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
"""
def user_profile(request):
  if request.method == 'POST':
    pass
  return render(request, 'profile.html')

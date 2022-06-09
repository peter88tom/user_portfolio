from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import  User
from user.models import Profile
from user.forms import UserForm



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


"""
 user signup
"""
def signup(request):
  if request.method == 'POST':
    form = UserForm(request.POST)

    # validate form inputs
    if form.is_valid():
      new_user = form.save()
      new_user.set_password(form.cleaned_data['password1'])
      new_user.is_active=True

      new_user.save()

      messages.success(request, 'Successfully registered, please login with your credentials')
      return redirect('login')

    messages.warning(request, 'Form not valid, please make sure both password matches')
    return redirect('signup')

  return render(request, 'signup.html')

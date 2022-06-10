from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
from django.http.response import JsonResponse

# models and form imports
from django.contrib.auth.models import User
from user.models import Profile
from user.forms import UserForm

# will be using this endpoint to get latitude and longitude when user updates their home address
API_KEY='493c254db58099a8ea029b5aed2e2b82'
END_POINT = 'http://api.positionstack.com/v1/'



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
  if request.user.is_authenticated:
    if request.method == 'POST':
      # update user profile
      user = User.objects.get(pk=request.user.id)
      user.first_name = request.POST['first_name']
      user.last_name = request.POST['last_name']
      user.profile.home_address = request.POST['home_address']
      user.profile.phone_number = request.POST['phone_number']

      """
        use home address to get the latitude and longitude  which will be used to
        create full screen map to show location of all registered users
      """
      req = requests.get(f"{END_POINT}forward?access_key={API_KEY}&query={request.POST['home_address']}")

      if req.status_code == 200:
        res = req.json()

        if len(res['data']) != 0:
          user.profile.latitude = res['data'][0]['latitude']
          user.profile.longitude = res['data'][0]['longitude']
        else:
          user.profile.latitude = '-'
          user.profile.longitude = '-'

      user.save()

      # redirect back to their profile
      messages.success(request, 'Profile updated successfully')
      return redirect('user-profile')

    return render(request, 'profile.html')

  messages.warning(request, 'You are not logged in')
  return redirect('login')


# signup page
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


# default page to show location of all registered users
def map_to_show_registered_users(request):
  if request.user.is_authenticated:
    return render(request, 'map.html')

  messages.warning(request, 'You are not logged in')
  return redirect('login')


# return json response for user location
def get_users_latitude_and_longitude(request):
  if request.user.is_authenticated:
    data = []
    locations = Profile.objects.all()

    for location in locations:
      k = {
        'lat':location.latitude,
        'long':location.longitude,
        'first_name': location.user.first_name,
        'home_address':location.home_address,
        'phone':location.phone_number,
      }

      data.append(k)

    return JsonResponse(data, safe=False)

  messages.warning(request, 'You are not logged in')
  return redirect('login')

from django.shortcuts import render


# Default page for the application
def login_index(request):
  return render(request, 'index.html')

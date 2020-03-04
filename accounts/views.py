from django.shortcuts import render, redirect, reverse
from django.contrib import auth

# Create your views here.

# create a view function called index and its going to take in a request

def index(request):
  """Return the index.html file and pass in the request and the name of the html file that we want to serve"""
  return render(request, 'index.html')

def logout(request):
  """Log the user out"""
  auth.logout(request)
  return redirect(reverse('index'))
  # reverse allows us to pass the name of a url instead of a name of a view

from django.shortcuts import render

# Create your views here.

# create a view function called index and its going to take in a request

def index(request):
  """Return the index.html file and pass in the request and the name of the html file that we want to serve"""
  return render(request, 'index.html')

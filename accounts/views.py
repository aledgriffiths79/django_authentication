from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm


# Create your views here.

# create a view function called index and its going to take in a request

def index(request):
  """Return the index.html file and pass in the request and the name of the html file that we want to serve"""
  return render(request, 'index.html')

@login_required
def logout(request):
  """Log the user out"""
  auth.logout(request)
  messages.success(request, "You have successfully been logged out!")
  return redirect(reverse('index'))
  # reverse allows us to pass the name of a url instead of a name of a view

def login(request):
  """Return a login page"""
  if request.user.is_authenticated:
    return redirect(reverse('index'))
  if request.method == 'POST':
    login_form = UserLoginForm(request.POST)
    # retrieve the username from the POST dictionary, same for password. we will use the password key to retieve the password from the dictionary and this will authenticate the user
    if login_form.is_valid():
      user = auth.authenticate(username=request.POST['username'],
                               password=request.POST['password'])
      if user:
        auth.login(user=user, request=request)
        messages.success(request, "You have successfully logged in!")
        # after a user has successfully logged in what we want to do is we want
        # to redirect them to a specific page just so that they're not redirected back to
        # the login page
        return redirect(reverse('index'))
      else:
        login_form.add_error(None, 'Your username or password is incorrect!')
  else:
    login_form = UserLoginForm()

  # create an instance of the loginform
  return render(request, 'login.html', {'login_form': login_form})

# implementing a registration functonality
# (request) is a object and parameter i think

def registration(request):
  """Render the registration page"""
  if request.user.is_authenticated:
    return redirect(reverse('index'))

  # check if the request.method was a post
  if request.method == 'POST':
    # if it is a post we need to instantiate the registration form using the values contained within the request post method
    registration_form = UserRegistrationForm(request.POST)

    if registration_form.is_valid():
      registration_form.save()

      user = auth.authenticate(username=request.POST['username'],
                               password=request.POST['password1'])

      if user:
        auth.login(user=user, request=request)
        messages.success(request, 'You have successfully registered')
      else:
        messages.error(request, 'Unable to register your account at this time')
  else:
    # create an instance of the registration form
    registration_form = UserRegistrationForm()
  return render(request, 'registration.html', {
      'registration_form': registration_form})

def user_profile(request):
  """The users profile page"""
  """Here we retrieve the user from the database"""
  user = User.objects.get(email=request.user.email)
  return render(request, 'profile.html', {'profile': user})




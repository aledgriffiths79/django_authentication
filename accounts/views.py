from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm


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

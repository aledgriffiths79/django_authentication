from django import forms
from django.contrib.auth.models import User
# usercreationform is a base form that django provides us and it will give us user names and emails
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


# the forms section for registration requires us to store some info in the database about the user. To achieve this we're going to from django.contrib.auth.models import user. This will import the user model provided by Django
# create a form object

class UserLoginForm(forms.Form):
  """inherit from forms.Form"""
  """Form to be used to log users in"""
  """inside or constructor, widget will tell django that we want to render a normal text input box but we want it to be of type password"""
  # constructor
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)

# this form will inherit from usercreationform this will give us the username and email fields
class UserRegistrationForm(UserCreationForm):
  """Form used to register a new user"""

  password = forms.CharField(widget=forms.PasswordInput)
  password2 = forms.CharField(
      label="Password Confirmation", 
      widget=forms.PasswordInput)

  # inner class Meta
  class Meta:
    model = User
    fields = ['email', 'username', 'password1', 'password2']

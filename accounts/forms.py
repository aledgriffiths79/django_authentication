from django import forms

# create a form object

class UserLoginForm(forms.Form):
  """inherit from forms.Form"""
  """Form to be used to log users in"""
  """inside or constructor, widget will tell django that we want to render a normal text input box but we want it to be of type password"""
  # constructor
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)
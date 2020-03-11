# So up until now what we've usually been doing is putting all of our URLs and our urls.py file in the project as opposed to a app specific URLs file. So we are going to create another urls.py file inside of the accounts app

from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile
from accounts import url_reset

# create a url patterns list

urlpatterns = [
  url(r'^logout/$', logout, name='logout'),
  url(r'^login/$', login, name='login'),
  # we will pass through the registration view and we will give the view a name of registration
  url(r'^register/$', registration, name='registration'),
  # user_profile underneath connects to the view function def user_profile and must include it above from accounts.view import user_profile
  url(r'^profile/$', user_profile, name='profile'),
  url(r'^password-reset/', include(url_reset))
]




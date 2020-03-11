from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

# create a list called urlpatterns
#  Example of what the first url is doing: post reset redirect and that's gonna redirect to the password reset done view. we're gonna give this URL a name so we call it password reset 

urlpatterns = [
  url(r'^$', password_reset,{'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
  url(r'^done/$', password_reset_done, name='password_reset_done'),
  # we need to create a unique URL for each password reset, below
  url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
  {'post_reset_confirm': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
  url(r'^complete/$', password_reset_complete, name='password_reset_complete')
]

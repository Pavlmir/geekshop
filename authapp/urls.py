from django.urls import re_path

from authapp.views import login, register, logout, profile, verify

app_name = 'authapp'

urlpatterns = [
    re_path(r"^login/$", login, name='login'),
    re_path(r"^logout/$", register, name='register'),
    re_path(r"^register/$", logout, name='logout'),
    re_path(r"^edit/$", profile, name='profile'),
    re_path(r"^verify/(?P<email>.+)/(?P<activation_key>\w+)/$", verify, name="verify"),
]
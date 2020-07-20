
from django.urls import re_path

from . import views

app_name = 'user'

urlpatterns = [
    re_path(r'^index/$', views.index),
    re_path(r'^index1/$', views.index1, name='index1'),
    re_path(r'^say/$', views.say, name='say'),
]

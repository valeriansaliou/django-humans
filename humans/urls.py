from django.conf.urls import *

from humans import views

urlpatterns = patterns('',
    url(r'$', views.humans, name='humans'),
)

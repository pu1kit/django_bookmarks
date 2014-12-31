from django.conf.urls import patterns, include, url
from django.contrib import admin
from bookmarks.views import *

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'django_bookmarks.views.home', name='home'),
                       url(r'^$', main_page),



                       )

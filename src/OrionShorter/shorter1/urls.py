'''
Created on 29/01/2011

@author: ThiagoP
'''

from django.conf.urls.defaults import *

import views


urlpatterns = patterns('',
                       url('^$', views.home),
                       url('^short', views.short),
                       url('^.{1,6}$', views.get)
                       )

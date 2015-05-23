#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from . import views

urlpatterns = [
	# url(r'^$', views.main_page),
    url(r'^$', views.album_list),
    url(r'^album/(?P<album_id>[0-9]+)/$', views.album_detail),
    url(r'^stats/', views.stats),
]
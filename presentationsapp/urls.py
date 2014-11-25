from django.conf.urls import patterns, url

from presentationsapp import views

urlpatterns = patterns('',
	#url(r'^(?P<course_id>[0-9]+)/$', views.courseDetails),
	url(r'^login/$', views.login),
	url(r'^register/$', views.register),
	url(r'^logout/$', views.logout),
	url(r'^create/$', views.create),
	url(r'^presentation/(?P<id>[0-9]+)/$', views.presentation),
	url(r'^present/(?P<id>[0-9]+)/$', views.present),
	url(r'^control/(?P<id>[0-9]+)/start/$', views.control_start),
	url(r'^control/(?P<id>[0-9]+)/end/$', views.control_end),
	url(r'^control/(?P<id>[0-9]+)/next/$', views.control_next),
	url(r'^control/(?P<id>[0-9]+)/prev/$', views.control_prev),
	url(r'^$', views.index),
)

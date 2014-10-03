from django.conf.urls import patterns, url

from presentationsapp import views

urlpatterns = patterns('',
	#url(r'^(?P<course_id>[0-9]+)/$', views.courseDetails),
	url(r'^login/$', views.login),
	url(r'^register/$', views.register),
	url(r'^logout/$', views.logout),
	url(r'^create/$', views.create),
	url(r'^$', views.index),
)

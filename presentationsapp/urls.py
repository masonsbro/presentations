from django.conf.urls import patterns, url

from presentationsapp import views

urlpatterns = patterns('',
	#url(r'^(?P<course_id>[0-9]+)/$', views.courseDetails),
	url(r'^$', views.index),
)

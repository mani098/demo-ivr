from django.conf.urls import patterns, url

from ivr_call import views

urlpatterns = patterns('',
	url(r'^response/ivr/$', views.ivr, name='ivr_response'),
	url(r'^response/redirect/$', views.ivr_redirect, name='ivr_redirect'),
	url(r'^$', views.index, name='homeview'),
	)
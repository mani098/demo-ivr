from django.conf.urls import patterns, url

from ivr_call import views

urlpatterns = patterns('',
	url(r'^response/ivr/$', views.ivr, name='ivr_response'),
	url(r'^$', views.index, name='homeview'),
	)
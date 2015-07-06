from django.conf.urls import patterns, url

from ivr_call import views

urlpatterns = patterns('',
	url(r'^response/ivr/$', views.ivr, name='ivr_response'),
	url(r'^response/redirect/$', views.ivr_redirect, name='ivr_redirect'),
	url(r'^option/delete/$', views.option_delete, name='option_delete'),
	url(r'^$', views.index, name='homeview'),
	)
from django.conf.urls import patterns, url

from assignment import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),

	url(r'^(?P<game_id>\d+)/$', views.detail, name='detail'),

	url(r'^(?P<game_id>\d+)/results/$', views.results, name='results'),

	url(r'^(?P<game_id>\d+)/signup/$', views.signup, name='signup'),

)

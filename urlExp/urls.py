from django.conf.urls import url
from . import views
from rest_framework.authtoken import views as view3
from django.conf.urls import include

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
	url(r'^urls/$', views.url_list),
	url(r'^urls/(?P<pk>[0-9]+)/$', views.url_detail),
	url(r'^api-token-auth/', view3.obtain_auth_token),



]
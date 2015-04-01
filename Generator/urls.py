from django.conf.urls import patterns, url
from Generator import views

urlpatterns=patterns('',
	url(r'^$',views.index,name='index'),
	url(r'^generated/$', views.generated, name="generated"),
	url(r'^undo-model/$',views.undo, name="undo-model"),


	)
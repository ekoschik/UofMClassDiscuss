from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'classDiscuss.views.home', name='home'),

	#direct calls through the framwork to UMICH.IO
    url(r'^subj_list/', 'classDiscuss.views.getSubjectList'),
	url(r'^class_list/(?P<subject>\w{0,50})/$', 'classDiscuss.views.getClassList'),
	url(r'^class_info/(?P<classnum>\w{0,50})/$', 'classDiscuss.views.getClassInfo'),   
)

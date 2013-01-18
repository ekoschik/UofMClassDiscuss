from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'classDiscuss.views.home', name='home'),

	#direct calls through the framwork to UMICH.IO
    url(r'^department_list/', 'classDiscuss.views.getDepartmentList'),
	url(r'^class_list/(?P<department>\w{0,50})/$', 'classDiscuss.views.getClassList'),
	url(r'^class_info/(?P<department>\w{0,50})/(?P<classnum>\w{0,50})/$', 'classDiscuss.views.getClassInfo'),  
)

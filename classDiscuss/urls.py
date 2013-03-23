from django.conf.urls import patterns, include, url

from jsonrpc import jsonrpc_site
from classDiscuss.views import addUserToClass

urlpatterns = patterns('',
	url(r'^fandjango/', include('fandjango.urls')),	
	url(r'^/addclass/$', 'classDiscuss.views.addUserToClass', name='addUserToClass'),
	
	#HTML pages
	url(r'^$', 'classDiscuss.views.home', name='home'),
	url(r'^profile/(?P<fbid>\w{0,50})/$', 'classDiscuss.views.profile'),
	url(r'^class/(?P<depcode>\w{0,50})/(?P<classnum>\w{0,50})/$', 'classDiscuss.views.class_page'),

	#UMICH_IO
    url(r'^department_list/', 'classDiscuss.views.getDepartmentList'),
	url(r'^class_list/(?P<department>\w{0,50})/$', 'classDiscuss.views.getClassList'),
	url(r'^class_info/(?P<department>\w{0,50})/(?P<classnum>\w{0,50})/$', 'classDiscuss.views.getClassInfo'),  
)

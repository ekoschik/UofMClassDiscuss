from django.conf.urls import patterns, include, url
from jsonrpc import jsonrpc_site
import classDiscuss.views

urlpatterns = patterns('',
	url(r'^fandjango/', include('fandjango.urls')),	
	
	#HTML pages
	url(r'^$', 'classDiscuss.views.home', name='home'),
	url(r'^profile/(?P<fbid>\w{0,50})/$', 'classDiscuss.views.profile'),
	url(r'^class/(?P<depcode>\w{0,50})/(?P<classnum>\w{0,50})/$', 'classDiscuss.views.class_page'),

	#RPCs
	url(r'^addclass/$', 'classDiscuss.views.add_class'),
	url(r'^dropclass/$', 'classDiscuss.views.drop_class'),
	url(r'^updatecomment/$', 'classDiscuss.views.update_comment'),
	

	#UMICH_IO
    url(r'^department_list/', 'classDiscuss.views.getDepartmentList'),
	url(r'^class_list/(?P<department>\w{0,50})/$', 'classDiscuss.views.getClassList'),
	url(r'^class_info/(?P<department>\w{0,50})/(?P<classnum>\w{0,50})/$', 'classDiscuss.views.getClassInfo'),  
)

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'classDiscuss.views.home', name='home'),

    url(r'^subj_list/', 'classDiscuss.views.getSubjectList'),
	url(r'^class_list/(?P<subject>\w{0,50})/$', 'classDiscuss.views.getClassList'),
       
)

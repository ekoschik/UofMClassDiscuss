from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext
import requests
import json

def getSubjectList(request):

	if request.method == 'GET':
		r=requests.get('http://umich.io/academics/v0/subjects')
		return r.text
	else:
		return HttpResponse('Must Use POST.')

def getClassList(request, subject):
	r=requests.get('http://umich.io/academics/v0/'+subject+'/courses')
	return r.text #returns json in string form
	return HttpResponse(subject)

def home(request):
	data={}
#	data['subjects'] = json.loads(getSubjectList())
	#return render_to_response('home.html', data, RequestContext(request))
	return render_to_response('home.html')
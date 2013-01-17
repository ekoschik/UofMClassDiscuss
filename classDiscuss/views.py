from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext
import requests
import json


def home(request):
	return render_to_response('home.html')


def getSubjectList(request):
	if request.method == 'GET':
		r=requests.get('http://umich.io/academics/v0/subjects')
		return HttpResponse(r.text,mimetype='application/json')
	else:
		return HttpResponse('Must Use GET.')

def getClassList(request, subject):
	if request.method == 'GET':
		r=requests.get('http://umich.io/academics/v0/'+subject+'/courses')
		return HttpResponse(r.text,mimetype='application/json')
	else:
		return HttpResponse('Must Use GET.')

def getClassInfo(request, classnum):
	if request.method == 'GET':
		r=requests.get('http://umich.io/academics/v0/'+classnum+'/info')
		return HttpResponse(r.text,mimetype='application/json')
	else:
		return HttpResponse('Must Use GET.')




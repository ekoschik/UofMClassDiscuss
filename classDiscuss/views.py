from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext
import requests
import json


def home(request):
    return render_to_response('home.html')


def getDepartmentList(request):
    if request.method == 'GET':
        r = requests.get('http://umich.io/academics/v0/subjects')
        return HttpResponse(r.text, mimetype = 'application/json')
    else:
        return HttpResponse('Must Use GET.')


def getClassList(request, department):
    if request.method == 'GET':
        r = requests.get('http://umich.io/academics/v0/' + department + '/courses')
        return HttpResponse(r.text, mimetype='application/json')
    else:
        return HttpResponse('Must Use GET.')


def getClassInfo(request, department, classnum):
    if request.method == 'GET':
        r = requests.get('http://umich.io/academics/v0/' + department + '/' + classnum + '/sections')
        return HttpResponse(r.text, mimetype = 'application/json')
    else:
        return HttpResponse('Must Use GET.')




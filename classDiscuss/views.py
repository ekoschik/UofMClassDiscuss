from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
import requests
import json
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages

from social_auth import __version__ as version
from social_auth.utils import setting
from fandjango.decorators import facebook_authorization_required




@facebook_authorization_required
def home(request):
    return render_to_response('home.html')
    #return HttpResponse('Hi, %s!' % request.facebook.user.facebook_id)

@facebook_authorization_required
def addUserToClass(request):
    request.facebook.user.facebook_id





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




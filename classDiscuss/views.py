from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages
from social_auth import __version__ as version
from social_auth.utils import setting
from fandjango.decorators import facebook_authorization_required
import requests
import json
from django.conf.urls.defaults import *
from classDiscuss.models import Class, ClassComment
from jsonrpc import jsonrpc_method
from django.template import loader, Context

#Main Page
@facebook_authorization_required
def home(request):
    c=Context({ 'fbid':request.facebook.user.facebook_id,
                'name':request.facebook.user.first_name
    })
    t=loader.get_template('home.html')
    return HttpResponse(t.render(c))


@facebook_authorization_required
def profile(request, fbid):
    prompt = 'User ' + str(request.facebook.user.facebook_id)
    prompt += ' looking for profile '
    prompt += str(fbid)
    return HttpResponse(prompt)


@facebook_authorization_required
def class_page(request, depcode, classnum):
    prompt = 'User ' + str(request.facebook.user.facebook_id)
    prompt += ' looking for class '
    prompt += str(classid)
    return HttpResponse(prompt)


 
#RPCs
def createClassComment(user_fbid, depcode, classnum, classname, given_year, given_semester):
    '''Creates a class and a class comment, erroring out if they exist already'''

    try:
        c = Class.objects.get(department=depcode, className=classnum)
    except MultipleObjectsReturned:
        return "ERROR Multiple classes found on lookup!"
    except ObjectDoesNotExist:
        c = Class(department=depcode, classNum=classnum, className=classname)
        c.save()

    try:
        cc = ClassComment.objecs.get(fbid=user_fbid, classobj=c)
    except MultipleObjectsReturned:
        return "ERROR Multiple class comments returned!"
    except ObjectDoesNotExist:
        cc = ClassComment(fbid=user_fbid, classobj=c, year=given_year, semester=given_semester)
        cc.save()

    return "success"

@jsonrpc_method('myapp.addclass', authenticated=True)
def addUserToClass(request):
    if request.method != 'POST':
        return 'Must Use POST'

    fbid = request.facebook.user.facebook_id
    g_depcode = request.POST['depcode']
    g_classnum = request.POST['classnum']
    g_classname = request.POST['classname']
    g_year = request.POST['year']
    g_semester = request.POST['semester']

    return createClassComment(fbid, g_depcode, g_classnum, g_classname, g_year, g_semester)
    




def removeClassComment(user_fbid, depcode, classnum):
    '''Finds Class Comment and deletes it, erroring out if not found'''

    try:
        c = Class.objects.get(department=depcode, classNum=classnum)
    except MultipleObjectsReturned:
        return "ERROR Multiple Classes Found on Lookup!"
    except ObjectDoesNotExist:
        return "Class Not Found"

    try:
        cc = ClassComment.objects.get(fbid=user_fbid, classobj=c)
        cc.delete();
    except MultipleObjectsReturned:
        return "ERROR Multiple Class Comments Found on Lookup!"
    except ObjectDoesNotExist:
        return "Class Comment Not Found"

    return "success"



























#Forwarded calls to UMICH.IO

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




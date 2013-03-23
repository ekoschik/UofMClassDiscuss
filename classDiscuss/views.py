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
from classDiscuss.models import ClassComment
from jsonrpc import jsonrpc_method
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from facepy import GraphAPI

@facebook_authorization_required
def home(request):
    u_fbid = request.facebook.user.facebook_id
    clist=ClassComment.objects.filter(fbid=u_fbid)

    c=Context({ 'fbid':u_fbid,
                'name':request.facebook.user.first_name,
                'comment_list':clist})

    t=loader.get_template('home.html')
    return HttpResponse(t.render(c))


@facebook_authorization_required
def class_page(request, depcode, classnum):
    u_fbid = request.facebook.user.facebook_id
    clist=ClassComment.objects.filter(department=depcode, classNum=classnum)

    graph=GraphAPI(request.facebook.user.oauth_token.token)
    friends=graph.get('me/friends')

    c=Context({ 'fbid':u_fbid,
                'name':request.facebook.user.first_name,
                'comment_list':clist,
                'friends':friends})

    t=loader.get_template('class.html')
    return HttpResponse(t.render(c))


@facebook_authorization_required
def profile(request, fbid):
    prompt = 'User ' + str(request.facebook.user.facebook_id)
    prompt += ' looking for profile '
    prompt += str(fbid)
    return HttpResponse(prompt)


@facebook_authorization_required
@csrf_exempt
def update_comment(request):
    if request.method != 'POST':
        return HttpResponse('Must Use POST')

    fbid = request.facebook.user.facebook_id

    depcode = request.POST['depcode']
    classnum = request.POST['classnum']
    text = request.POST['text']
    
    count = ClassComment.objects.filter(fbid=fbid, department=depcode,classNum=classnum).count()
    if count > 1:
        return HttpResponse("ERROR Multiple comments found on lookup!")
    elif count == 1:
        cc = ClassComment.objects.filter(fbid=fbid, department=depcode,classNum=classnum).update(comment_text=text)
    else:
        return HttpResponse("ERROR no comment found")

    return HttpResponse('success')


@facebook_authorization_required
@csrf_exempt
def add_class(request):
    if request.method != 'POST':
        return HttpResponse('Must Use POST')

    fbid = request.facebook.user.facebook_id
    depcode = request.POST['depcode']
    classnum = request.POST['classnum']
    classname = request.POST['classname']

    count = ClassComment.objects.filter(fbid=fbid, department=depcode,classNum=classnum).count()
    if count > 1:
        return HttpResponse("ERROR Multiple comments found on lookup!")
    elif count == 1:
        return HttpResponse("duplicate")
    else:
        cc = ClassComment(fbid=fbid, department=depcode,classNum=classnum,className=classname)
        cc.save()
        
    return HttpResponse("success")


@facebook_authorization_required
@csrf_exempt
def drop_class(request): #user_fbid, depcode, classnum
    if request.method != 'POST':
        return 'Must Use POST'
    fbid = request.facebook.user.facebook_id
    depcode = request.POST['depcode']
    classnum = request.POST['classnum']

    count = ClassComment.objects.filter(fbid=fbid, department=depcode,classNum=classnum).count()
    if count > 1:
        return HttpResponse("ERROR Multiple comments found on lookup!")
    elif count == 1:
        cc = ClassComment.objects.get(fbid=fbid, department=depcode,classNum=classnum)
        cc.delete()
        return HttpResponse("success")
    else:
        return HttpResponse("ERROR no comment found")


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




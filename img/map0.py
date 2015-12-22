# -*- coding: cp936 -*-
#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from img.models import imagess, t
from django.template import Context, RequestContext
from PIL import Image
import StringIO
import string
import os
import sys
import time
sys.setdefaultencoding("utf-8")
sys.path.append('../')
from photo import settings
@csrf_exempt
def mapp(request):
    A = []
    from sae.storage import Bucket
    bucket = Bucket('abc')
    if request.GET:
        if request.GET.has_key('dtitle'):
            name = request.GET['dtitle']
            A = imagess.objects.filter(title = name)
    else:
        a = bucket.list(path='stati/')
        for i in a:
            s = i.name.split('/')[-1]
            ta = imagess.objects.filter(title = s)
            if (len(ta)!= 0):
                A.append(ta[0])
    return render_to_response('map.html',{'A':A },\
                              context_instance=RequestContext(request)) 
            









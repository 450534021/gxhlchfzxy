# -*- coding: cp936 -*-
#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
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
#美化部分
def beauti(request):
    r = g = b = s = 0
    from sae.storage import Bucket
    bucket = Bucket('abc')
    aa = bucket.list(path='meihua/')
    for ii in aa:
        bucket.delete_object(ii.name)
    if request.GET:
        if request.GET.has_key('btitle'):
            b = request.GET['btitle']
        if request.GET.has_key('ptitle'):
            g = request.GET['ptitle']
    if request.POST:
        if request.POST.has_key('lvjing'):
            if request.FILES or request.GET.has_key('btitle'):
                if request.FILES:
                    f = request.FILES['file']
                    bucket.put_object('lvjing/'+f.name, f)
                    img = bucket.get_object_contents('lvjing/'+f.name)
                    s = 'lv' + str(f)
                elif request.GET.has_key('btitle'):
                    name = request.GET['btitle']
                    img = bucket.get_object_contents('stati/'+name)
                    s = 'lv' + name
                im = Image.open(StringIO.StringIO(img))
                im.getdata()
                out = im.split()
                imgout = StringIO.StringIO()
                out[0].save(imgout,"jpeg")
                img_data = imgout.getvalue()
                bucket.put_object('meihua/'+s, img_data)
        if request.POST.has_key('suotu'):
            if request.FILES or request.GET.has_key('btitle'):
                if request.FILES:
                    f = request.FILES['file']
                    bucket.put_object('suotu/'+f.name, f)
                    img = bucket.get_object_contents('suotu/'+f.name)
                    s = 'su' + str(f)
                elif request.GET.has_key('btitle'):
                    name = request.GET['btitle']
                    img = bucket.get_object_contents('stati/'+name)
                    s = 'su' + name
                im = Image.open(StringIO.StringIO(img))
                out = im.resize((128, 128))
                imgout = StringIO.StringIO()
                out.save(imgout,"jpeg")
                img_data = imgout.getvalue()
                bucket.put_object('meihua/'+s, img_data)

        if request.POST.has_key('xuanzhuan'):
            if request.FILES or request.GET.has_key('btitle'):
                if (request.POST['dushu'] != ''):
                    dushu = request.POST['dushu']
                    i = string.atoi(dushu)
                else:
                    i = 0
                if request.FILES:
                    f = request.FILES['file']   
                    bucket.put_object('xuanzhuan/'+f.name, f)
                    img = bucket.get_object_contents('xuanzhuan/'+f.name)
                    s = 'xu'+str(f)
                else: 
                    name = request.GET['btitle']
                    img = bucket.get_object_contents('stati/'+name)
                    s = 'xu'+name
                
  
                im = Image.open(StringIO.StringIO(img))
                out = im.rotate(i)
                imgout = StringIO.StringIO()
                out.save(imgout,"jpeg")
                img_data = imgout.getvalue()
                bucket.put_object('meihua/'+s, img_data)

        if request.POST.has_key('huidu1'):
            if request.FILES or request.GET.has_key('btitle'):
                if request.FILES:
                    f = request.FILES['file']
                    bucket.put_object('huidu1/'+f.name, f)
                    img = bucket.get_object_contents('huidu1/'+f.name)
                    s = 'h1' + str(f)
                else:
                    name = request.GET['btitle']
                    img = bucket.get_object_contents('stati/'+name)
                    s = 'h1' + name
                im = Image.open(StringIO.StringIO(img))
                im.getdata()
                out = im.split()
                if (len(out) >0):
                    imgout = StringIO.StringIO()
                    out[0].save(imgout,"jpeg")
                else:
                    im.save(imgout, 'jpeg')
                img_data = imgout.getvalue()
                bucket.put_object('meihua/'+s, img_data)

        if request.POST.has_key('huidu2'):
            if request.FILES or request.GET.has_key('btitle'):
                if request.FILES:
                    f = request.FILES['file']
                    bucket.put_object('huidu2/'+f.name, f)
                    img = bucket.get_object_contents('huidu2/'+f.name)
                    s = 'h2' + str(f)
                elif request.GET.has_key('btitle'):
                    name = request.GET['btitle']
                    img = bucket.get_object_contents('stati/'+name)
                    s = 'h2' + name
                im = Image.open(StringIO.StringIO(img))
                im.getdata()
                out = im.split()
                imgout = StringIO.StringIO()
                if (len(out) > 1):
                    out[1].save(imgout,"jpeg")
                else:
                    im.save(imgout, 'jpeg')
                img_data = imgout.getvalue()
                bucket.put_object('meihua/'+s, img_data)
        if request.POST.has_key('huidu3'):
            if request.FILES or request.GET.has_key('btitle'):
                if request.FILES:
                    f = request.FILES['file']
                    bucket.put_object('huidu3/'+f.name, f)
                    img = bucket.get_object_contents('huidu3/'+f.name)
                    s = 'h3' + str(f)
                elif request.GET.has_key('btitle'):
                    name = request.GET['btitle']
                    img = bucket.get_object_contents('stati/'+name)
                    s = 'h3' + name
                im = Image.open(StringIO.StringIO(img))
                im.getdata()
                out = im.split()
                imgout = StringIO.StringIO()
                if (len(out) > 2):
                    out[2].save(imgout,"jpeg")
                else:
                    im.save(imgout, 'jpeg')
                img_data = imgout.getvalue()
                bucket.put_object('meihua/'+s, img_data)
       
    return render_to_response('pilbeau.html',{'r':s, 's':b, 'g':g},\
                              context_instance=RequestContext(request))  

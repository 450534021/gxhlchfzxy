# -*- coding: cp936 -*-
#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from img.models import imagess, t
from django.template import Context, RequestContext
from PIL import Image
import StringIO
import string
import os
import sys
sys.setdefaultencoding("utf-8")
sys.path.append('../')
from photo import settings
@csrf_exempt

#管理云端
def manage(request):
    from sae.storage import Bucket
    bucket = Bucket('abc')
    sa = t.objects.all()
    for x in sa:
        x.delete()
    if request.GET:     #delete
        if request.GET.has_key('ctitle'):
            name = request.GET["ctitle"]
            bucket.delete_object('manage/'+name)
            bucket.delete_object('stati/'+name)
            ta = imagess.objects.filter(title = name)
            if (len(ta)!= 0):
                for i in ta:
                    i.delete()
        if request.GET.has_key('stitle'):  #save beautify
            name = request.GET["stitle"]
            if (name != '0'):
                new_name = name[2:]
                new_comment = '..'
                new_mood = '..'
                ta = imagess.objects.filter(title = new_name)
                if (len(ta)!= 0):
                    new_comment = ta[0].comment
                    new_mood = ta[0].mood
                    new_lat = ta[0].lat
                    new_lon = ta[0].lon
                new_photo = imagess(picture = 0, comment = new_comment, mood = new_mood, \
                title = name, lat = new_lat, lon = new_lon)
                new_photo.save()
                obj = bucket.get_object_contents('meihua/'+name)
                im = Image.open(StringIO.StringIO(obj))
                imgout = StringIO.StringIO()
                im.save(imgout,"jpeg")
                img_data = imgout.getvalue()
                bucket.put_object('stati/'+name, img_data)
                im = Image.open(StringIO.StringIO(obj))
                out = im.resize((128, 128))
                imgout = StringIO.StringIO()
                out.save(imgout,"jpeg")
                img_data = imgout.getvalue()
                bucket.put_object('manage/'+name, img_data)
       #陈列部分           
    A = []
    a = bucket.list(path='manage/')
    for i in a:
        dic = []
        s = i.name.split('/')[-1]
        dic.append(s)
        dic.append(i.last_modified)
        ta = imagess.objects.filter(title = s)
        if (len(ta)!= 0):
            dic.append(ta[0].mood)
            dic.append(ta[0].comment)
        A.append(dic)

    if request.GET:
        if request.GET.has_key('search'):#search
            if request.GET['writesearch'] != '':
                A=[]
                wcomment = request.GET['writesearch']
                result = imagess.objects.filter(comment = wcomment)
                for i in range(0, len(result)):
                    a = bucket.stat_object('manage/'+result[i].title)
                    dic = []
                    dic.append(result[i].title)
                    dic.append(a.last_modified)
                    dic.append(result[i].mood)
                    dic.append(result[i].comment)
                    A.append(dic)
    
    return render_to_response('manage.html',{'A':A },\
                              context_instance=RequestContext(request))  


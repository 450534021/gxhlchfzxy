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
sys.setdefaultencoding("utf-8")
sys.path.append('../')
from photo import settings

# Create your views here.
@csrf_exempt
#编辑部分
def edit0(request):
    pname = pcomment = pmood = newname = 0
    from sae.storage import Bucket
    bucket = Bucket('abc')
    if request.POST:
        if request.POST.has_key('correct'):
            if request.GET.has_key('atitle'):
                pname = request.GET['atitle']
                pn = t.objects.all()
                if (len(pn)!= 0):
                    pname = pn[0].title
                    for i in pn:
                        i.delete()
                we = imagess.objects.filter(title = pname)
                if (len(we)!= 0):
                    img = bucket.get_object_contents('stati/'+pname)
                    im = Image.open(StringIO.StringIO(img))
                    imgout = StringIO.StringIO()
                    im.save(imgout,"jpeg")
                    img_data = imgout.getvalue()
                    we[0].title = request.POST['cname']+'.jpg'
                    newname = we[0].title
                    if (newname != pname):
                        ne = t(title = newname)
                        ne.save()
                        bucket.put_object('stati/'+newname, img_data)
                        im = Image.open(StringIO.StringIO(img))
                        out = im.resize((128, 128))
                        imgout = StringIO.StringIO()
                        out.save(imgout,"jpeg")
                        img_data = imgout.getvalue()
                        bucket.put_object('manage/'+newname, img_data)
                        bucket.delete_object('manage/'+pname)
                        bucket.delete_object('stati/'+pname)
                    pname = newname
                    we[0].comment = request.POST['ccomment']
                    we[0].mood = request.POST['cmood']
                    we[0].save()
            pname = request.POST['cname']+'.jpg'
            pcomment = request.POST['ccomment']
            pmood = request.POST['cmood']
    elif request.GET.has_key('atitle'):
        if (pname == 0):
            pname = request.GET['atitle']
            p = t(title = pname)
            p.save()
            we = imagess.objects.filter(title = pname)
            if (len(we)!= 0):
                pcomment = we[0].comment
                pmood = we[0].mood
    if (pname!=0):
        pname = pname[:-4]
        
    return render_to_response('editt.html',{'pname':pname,'newname':newname, \
    'pmood': pmood, 'pcomment':pcomment},context_instance=RequestContext(request))   



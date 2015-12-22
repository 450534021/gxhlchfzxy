# -*- coding: cp936 -*-
#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from img.models import imagess, t
from django.template import Context, RequestContext
from PIL import Image
from PIL.ExifTags import TAGS
import StringIO
import string
import os
import sys
import time
sys.setdefaultencoding("utf-8")
sys.path.append('../')
from photo import settings
@csrf_exempt
def start(request):
    url = 0
    from sae.storage import Bucket
    bucket = Bucket('abc')
    if request.POST:
        if request.POST.has_key('save'):
            post = request.POST
            if request.FILES:
                f = request.FILES['file']
                new_img = imagess(picture = f, comment = post['writecomment'], mood = post['writemood'],\
                    title = str(f),lat = 0,lon = 0)
                new_img.save()
                img = bucket.get_object_contents('stati/'+f.name)
                im = Image.open(StringIO.StringIO(img))
                out = im.resize((128, 128))
                imgout = StringIO.StringIO()
                out.save(imgout,"jpeg")
                img_data = imgout.getvalue()
                bucket.put_object('manage/'+f.name, img_data)

                exif = get_exif_data(img)
                if exif.has_key('GPSInfo'):
                    w1 = exif['GPSInfo'][2][0][0]
                    w2 = exif['GPSInfo'][2][1][0]
                    w3 = exif['GPSInfo'][2][2][0]*1.0/100
                    lat = w1+w2*1.0/60 + w3*1.0/60*1.0/60
                    j1 = exif['GPSInfo'][4][0][0]
                    j2 = exif['GPSInfo'][4][1][0]
                    j3 = exif['GPSInfo'][4][2][0]*1.0/100
                    lon = j1+j2*1.0/60 + j3*1.0/60*1.0/60
                    new = imagess.objects.filter(title = f.name)
                    if (len(new) != 0):
                        new[0].lat = lat
                        new[0].lon = lon
                        new[0].save()


                
    return render_to_response('start.html',\
            context_instance=RequestContext(request))

def get_exif_data(fname):
    """Get embedded EXIF data from image file."""
    ret = {}
    try:
        img = Image.open(StringIO.StringIO(fname))
        if hasattr( img, '_getexif' ):
            exifinfo = img._getexif()
            if exifinfo != None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
    except IOError:
        print 'IOERROR ' + fname
    return ret
     
     






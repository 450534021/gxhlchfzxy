# -*- coding: cp936 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from img.models import imagess
from django.template import Context, RequestContext
import Image
import StringIO
import os
import sys
sys.path.append('../')
from photo import settings

# Create your views here.
def start(request):
    if request.POST:
        if request.POST.has_key('save'):
            post = request.POST
            f = request.FILES['file']
            aset = imagess.objects.filter(title = str(f))
            if len(aset)!= 0:
                #file_full_path = os.path.join(settings.MEDIA_ROOT, 'stati\\' + str(aset[0].picture))
                #os.remove(file_full_path)
                aset[0].delete()
                
            new_img = imagess(picture = f, comment = post['writecomment'], mood = post['writemood'],\
                              title = str(f))
            new_img.save()
            
        if request.POST.has_key('delete'):
            f = request.FILES['file']
            file_full_path = os.path.join(settings.MEDIA_ROOT, 'stati\\' + str(f))
            os.remove(file_full_path)
    return render_to_response('start.html',\
            context_instance=RequestContext(request))


from django.views.decorators.csrf import csrf_exempt
from webgui.models import ServerActivity as sa
from webgui.models import ServerList  as sl
from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.db import models
import json


@csrf_exempt
def server_activity(request):
    recived_data = dict()
    result={}
    if request.method == "POST":
        TokenCheck= sl.objects.filter(ServerToken=request.POST['ServerToken']).exists()
        if TokenCheck==True : 
            sa.objects.create(date=request.POST['date'],time=request.POST['time'],Status=request.POST['Status'],ServerID=request.POST['ServerID'],
            Hostname=request.POST['Hostname'],Activity=request.POST['Activity'],EndActivity=request.POST['EndActivity'],
            StartActivity=request.POST['StartActivity'])  
            result['status'] = '200 OK' 
        else : 
            result['status']='403 Forbidden'
        return HttpResponse(json.dumps(result), content_type="application/json")
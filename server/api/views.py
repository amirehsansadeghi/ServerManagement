from django.views.decorators.csrf import csrf_exempt
from webgui.models import ServerActivity as sa
from webgui.models import  ServerStatus as ss
from webgui.models import ServerList  as sl
from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
import json


@csrf_exempt
def server_activity(request):
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
    
@csrf_exempt
def server_status(request):
    result={}
    if request.method == "POST":
        TokenCheck= sl.objects.filter(ServerToken=request.POST['ServerToken']).exists()
        if TokenCheck==True:
            ss.objects.create(ServerID=request.POST['ServerID'],date=request.POST['date'],time=request.POST['time'],CPUUsage=request.POST['CPUUsage'],
            MemoryUsage=request.POST['MemoryUsage'],DiskUsage=request.POST['DiskUsage'],UpTime=request.POST['UpTime'],Health=request.POST['Health'])
            result['status'] = '200 OK'
        else : 
            result['status']='403 Forbidden'
    return HttpResponse(json.dumps(result), content_type="application/json")
    
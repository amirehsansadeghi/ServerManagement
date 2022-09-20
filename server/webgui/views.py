from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
# Create your views here.


def login(request):
    return render(request, "login.html")

def dashboard(request):
    context = {
        'CopyrightYear' : datetime.now().year,
        'title':'Server Management',
        'PersonName': request.user.first_name +' '+ request.user.last_name,
        'username': request.user
    }
    return render(request,"index.html",context)
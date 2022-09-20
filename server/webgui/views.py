from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None : 
            login(request,user)
            return render(request,"index.html")
    return render(request, "login.html")

#@login_required
def dashboard(request):
    context = {
        'CopyrightYear' : datetime.now().year,
        'title':'Server Management',
        'PersonName': request.user.first_name +' '+ request.user.last_name,
        'username': request.user
    }
    return render(request,"index.html",context)
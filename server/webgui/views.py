from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
from webgui.models import ServerActivity

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #if  request.POST.get('remember_me', None):
        #    request.session.set_expiry(1)
        #else:
        #    request.session.set_expiry(0)
        user = authenticate(username=username,password=password)
        if user is not None : 
            auth_login(request, user)
            context = {
        'CopyrightYear' : datetime.now().year,
        'title':'Server Management',
        'PersonName': request.user.first_name +' '+ request.user.last_name,
        'username': request.user,
        'ServerActivity' : ServerActivity.objects.all(),
        
        }
            return render(request,"index.html", context)
        else : 
            messages.error(request, "Bad Credentials!!")
            return redirect('login')
    return render(request, "login.html")

@login_required
def logout(request):
    auth_logout(request)
    return redirect('/webgui/login')

@login_required
def dashboard(request):
    context = {
        'CopyrightYear' : datetime.now().year,
        'title':'Server Management',
        'PersonName': request.user.first_name +' '+ request.user.last_name,
        'username': request.user,
        'ServerActivity' : ServerActivity.objects.all(),
        }
    return render(request,"index.html",context)



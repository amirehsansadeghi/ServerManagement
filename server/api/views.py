from django.shortcuts import render
from django.http import HttpResponse


def server_activity(request):
    return HttpResponse('salam')
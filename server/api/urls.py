from django.conf.urls.static import static 
from django.urls import path,include
from django.conf import settings 
from . import views

urlpatterns = [
    path('serveractivity',views.server_activity,name='server_activity'),

]

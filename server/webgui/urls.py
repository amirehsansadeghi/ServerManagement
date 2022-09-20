from django.conf.urls.static import static 
from django.conf import settings 
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login ),
    path('dashboard/',views.dashboard),
]

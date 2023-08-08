from django.conf.urls.static import static 
from django.urls import path,include
from django.conf import settings 
from . import views

urlpatterns = [
    path('',views.login ,name='login'),
    path('logout/',views.logout,name='logout'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashborad'),
    path('dashboard/controlpanel/',views.controlpanel,name='controlpanel')


]

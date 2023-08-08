from django.contrib import admin

from .models import ServerList,ServerStatus,ServerActivity


admin.site.register(ServerList)
admin.site.register(ServerStatus)
admin.site.register(ServerActivity)



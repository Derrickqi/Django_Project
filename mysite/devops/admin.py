from django.contrib import admin
from .models import UserInfo, HostInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'c_time']


class HostInfoAdmin(admin.ModelAdmin):
    list_display = ['ipaddr', 'hostname', 'status', 'information']


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(HostInfo, HostInfoAdmin)
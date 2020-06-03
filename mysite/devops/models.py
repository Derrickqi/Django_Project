from django.db import models



class UserInfo(models.Model):
    """用户信息"""

    username = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')
    email = models.EmailField(unique=True, verbose_name='邮箱')
    c_time = models.DateTimeField(auto_now_add=True)


class HostInfo(models.Model):
    """主机信息"""
    status_choice = ((0, 'downline'), (1, 'online'))
    ipaddr = models.GenericIPAddressField(protocol="ipv4", db_index=True, verbose_name='IP地址')
    hostname = models.CharField(max_length=32, db_index=True, verbose_name='主机名')
    status = models.SmallIntegerField(choices=status_choice, default=0, verbose_name='主机状态')
    information = models.TextField(max_length=128, verbose_name='备注')

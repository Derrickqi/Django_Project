# 导入 HttpResponse 模块
from django.shortcuts import render, redirect , 
import pymysql


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        u = request.POST.get('username', None)
        p = request.POST.get('password', None)
        if u == 'root' and p == '123123':
            return redirect('/index/')
        else:
            msg = '账户或密码不正确'
            return render(request, "login.html", {'msg': msg})


def index(request):
    import pymysql
    # 打开数据库连接
    db = pymysql.connect(host="192.168.190.134", port=3306, user="root", passwd="123456", db='mysql',
                         charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT id,ipaddr,hostname,status,information from devops_hostinfo")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()

    cursor.close()
    # 关闭数据库连接
    db.close()
    return render(request, "index.html", {'data': data})


def register(request):
    return render(request, 'register.html')


def logout(request):
    return render(request, 'index.html')


# 添加主机
def add_host(request):
    if request.method == 'GET':
        return render(request, 'add_host.html')
    else:
        print(request.POST)
        ipaddr = request.POST.get('ipaddr')
        hostname = request.POST.get('hostname')
        status = request.POST.get('status')
        information = request.POST.get('information')

        if len(ipaddr) > 0 and len(hostname) > 0 and len(status) > 0:
            db = pymysql.connect(host="192.168.190.134", port=3306, user="root", passwd="123456", db='mysql',
                                 charset='utf8')
            cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute(
                "insert into devops_hostinfo(ipaddr, hostname, status, information) values('%s','%s','%s','%s')" % (
                    ipaddr, hostname, status, information))
            db.commit()
            cursor.close()
            db.close()
            return redirect('/index/')
        else:
            return render(request, 'add_host.html', {"msg": "IP/hostname/status 不能为空值"})


from .sqlhelper import get_one, modify, delete


# 编辑主机
def edit_host(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        current_host_list = get_one("SELECT id,ipaddr,hostname,status,information from devops_hostinfo where id=%s",
                                    [nid, ])
        return render(request, 'edit_host.html', {'current_host_list': current_host_list})
    else:
        nid = request.POST.get('nid')
        ipaddr = request.POST.get('ipaddr')
        hostname = request.POST.get('hostname')
        status = request.POST.get('status')
        information = request.POST.get('information')
        print(nid, ipaddr, hostname, status, information)
        modify("update devops_hostinfo set ipaddr=%s,hostname=%s,information=%s,status=%s where id=%s",
               [ipaddr, hostname, information, status, nid, ])
        return redirect('/index/')


# 删除主机

def delete_host(request):
    nid = request.GET.get('nid')

    delete("delete from devops_hostinfo where id=%s", [nid, ])
    return redirect('/index/')

__author__ = 'Administrator'

import pymysql


def get_list(sql):
    # 打开数据库连接
    db = pymysql.connect(host="192.168.253.128", port=3306, user="root", passwd="123456", db='mysql',
                         charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()

    cursor.close()
    # 关闭数据库连接
    db.close()
    return data


def get_one(sql, args):
    # 打开数据库连接
    db = pymysql.connect(host="192.168.253.128", port=3306, user="root", passwd="123456", db='mysql',
                         charset='utf8')
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    data = cursor.fetchone()
    cursor.close()
    db.close()
    return data


def modify(sql, args):
    # 打开数据库连接
    db = pymysql.connect(host="192.168.253.128", port=3306, user="root", passwd="123456", db='mysql',
                         charset='utf8')
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    db.commit()
    cursor.close()
    db.close()


def delete(sql, args):
    # 打开数据库连接
    db = pymysql.connect(host="192.168.253.128", port=3306, user="root", passwd="123456", db='mysql',
                         charset='utf8')
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    db.commit()
    cursor.close()
    db.close()

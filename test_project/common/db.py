#coding=utf-8
#数据库查询模块
#import cx_Oracle
import MySQLdb
from .constant import *

def create_conn(dbtype='orcl',dbname='USR_ZONE_INTEG', dbuser='usr_zone_integ',dbpasswd='usr_zone_integ', dbip='172.17.210.45',dbport= 1521,dbsid='orcl'):
    '''创建数据库连接'''
    '''
    if (dbtype=='orcl'):
        dbip_sid = dbip+':'+dbport+'/'+dbsid
        conn = cx_Oracle.connect(dbname, dbpasswd, dbip_sid)
    '''
    if(dbtype=='mysql'):
        conn = MySQLdb.connect(host=dbip, port=dbport, user=dbuser, passwd=dbpasswd, db =dbname)
    return conn

def select(conn,sql,type='one'):
    '''查询语句,%s为占位符---格式：db.select('select STORE_NO from store p where p.status ='0' and p.store_no_dc='%s'" % strLocNo')'''
    cur = conn.cursor()
    try:
        cur.execute(sql)
        if(type=='one'):
            result = cur.fetchone()
        if(type=='all'):
            result = cur.fetchall()
        return result
    except conn.error as e:
        print (e)
    cur.close()
    conn.close()

def update(conn,sql):
    '''更新语句，包含插入/更新/删除'''
    cur = conn.cursor()
    try:
       cur.execute(sql)
       conn.commit()
    except conn.error as e:
       conn.rollback()
       print (e)
    cur.close()
    conn.close()


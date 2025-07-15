#!/usr/bin/python
# -*- coding: UTF-8 -*-
# coding=utf-8

import os
import sys
import datetime
import pprint

import pymysql

import pandas as pd
from pandas.io.json import json_normalize

#from signal import signal, SIGPIPE, SIG_DFL
#signal(SIGPIPE,SIG_DFL) 

# iDiving資料庫參數設定
db_homeSettings157 = {
    "host": "192.168.5.157",
    "port": 3306,
    "user": "admin",
    "password": "admin220",
    "db": "iDiving",
    "charset": "utf8"
}

db_homeSettingsRP357 = {
    "host": "192.168.12.57",
    "port": 3306,
    "user": "admin",
    "password": "admin220",
    "db": "iDiving",
    "charset": "utf8"
}


db_iDivingdbSettings57 = {
    "host": "192.168.12.57",
    "port": 3306,
    "user": "admin",
    "password": "admin220",
    "db": "iDiving_Test",
    "charset": "utf8"
}

jsonMachineRollCall = {
    "machineName": "",
    "machineGroup": "",
    "machineItem": "",
    "time": ""
}

serverName = {
    "host": "",
    "port": 0,
    "user": "",
    "password": "",
    "db": "",
    "charset": ""
}

class MysqliDivingStore():
    def __init__(self, machineGroup, mysql_name):
        print("MysqlStore__init__")
        print("MysqlStore__init___mysql_name:", mysql_name)
        if (machineGroup == 'ahome' and mysql_name == 'taibonii'):
            # 建立Connection物件
            self.conn = pymysql.connect(**db_homeSettings157)
            #print("MysqlStore__init->self.conn", self.conn)
            self.mysql_name = mysql_name
            self.machineGroup = machineGroup
        elif (machineGroup == 'ahome' and mysql_name == 'idiving'):
            # 建立Connection物件
            self.conn = pymysql.connect(**db_homeSettings157)
            #print("MysqlStore__init->self.conn", self.conn)
            self.mysql_name = mysql_name
            self.machineGroup = machineGroup
        elif (machineGroup == 'idiving' and mysql_name == 'taibonii'):
            # 建立Connection物件
            self.conn = pymysql.connect(**db_iDivingdbSettings57)
            #print("MysqlStore__init->self.conn", self.conn)
            self.mysql_name = mysql_name
            self.machineGroup = machineGroup
        elif (machineGroup == 'idiving' and mysql_name == 'idiving'):
            # 建立Connection物件
            self.conn = pymysql.connect(**db_iDivingdbSettings57)
            print("MysqlStore__init->self.conn", self.conn)
            self.mysql_name = mysql_name
            self.machineGroup = machineGroup


    # Test ==================================================
    def mysqlKsisauthNamePasswordTest(self):
        print("mysqlKsisauthNamePasswordTest")
        return "mysqlKsisauthNamePasswordTest"

    def mysqltaiboniitest(self):
        print("mysqltestinit")
        return "sdsd"


    # Test_01 ==================================================
    def mysqlTest01(self):
        print("mysqlTest01")
        return "mysqlTest01"

    # iDiving ==================================================
    # 點名 ==================================================
    def RollCallWrite(self, jsonMachineRollCall):
        print("RollCallWrite")
        
        print('jsonMachineRollCall ', jsonMachineRollCall)
        my_pmachineName = jsonMachineRollCall['machineName']
        my_pmachineGroup = jsonMachineRollCall['machineGroup']
        my_pmachineItem = jsonMachineRollCall['machineItem']
        my_ptime = jsonMachineRollCall['time']
        
        print('self.mysql_name-', self.mysql_name)
        
        #conn = pymysql.connect(**db_homeSettings157)
        
        mycursor = self.conn.cursor()
        
        sql = "INSERT INTO MachineRollCall (machineName, machineGroup, machineItem, time) VALUES (%s, %s, %s, %s)"
        val = (my_pmachineName, my_pmachineGroup, my_pmachineItem, my_ptime)
        stock = False
        stock = mycursor.execute(sql, val)
        
        print(stock)
        
        self.conn.commit()
        
        return stock
    
    
    # 04課程表單 ==================================================
    
    # PersonnelInformation ==================================================
    def PersonnelInformationRead(self):
        print("PersonnelInformationRead")
        # 建立Connection物件
        conn = pymysql.connect(**db_homeSettings157)
        
        strsearch = 'SELECT * FROM PersonnelInformation Limit 100;'
        
        stock = pd.read_sql(strsearch, con = conn)
        
        #print(stock)
        
        return stock
        
    # PersonnelInformation Single transaction 單筆==================================================
    def PersonnelInformationSingleRead(self, mid):
        print("PersonnelInformationRead")
        # 建立Connection物件
        conn = pymysql.connect(**db_homeSettings157)
        
        strsearch = 'SELECT * FROM PersonnelInformation WHERE (mid LIKE "%{my_pData01}%" );'.format(my_pData01=urllib.unquote(mid).encode('utf-8').strip())
        print(strsearch)
        stock = pd.read_sql(strsearch, con = conn)
        
        #print(stock)
        
        return stock
    
    # PersonnelInformation 01 ==================================================
    def PersonnelInformationRead01(self, name):
        print("PersonnelInformationRead01")
        # 建立Connection物件
        conn = pymysql.connect(**db_homeSettings157)
        
        strsearch = 'SELECT * FROM PersonnelInformation WHERE ( chineseName LIKE "%{my_pData01}%") OR ( remark LIKE "%{my_pData01}%");'.format(my_pData01=urllib.unquote(name).encode('utf-8').strip())
        
        print(strsearch)
        
        stock = pd.read_sql(strsearch, con = conn)
        
        #print(stock)
        
        return stock
        
    # Course ==================================================
    def CourseRead(self):
        print("CourseRead")
        # 建立Connection物件
        conn = pymysql.connect(**db_homeSettings157)
        
        strsearch = 'SELECT * FROM Course;'
        
        stock = pd.read_sql(strsearch, con = conn)
        
        #print(stock)
        
        return stock
        
    # Course ==================================================
    def CourseRead01(self):
        print("CourseRead01")
        # 建立Connection物件
        conn = pymysql.connect(**db_homeSettings157)
        
        strsearch = 'SELECT * FROM Course;'
        
        stock = pd.read_sql(strsearch, con = conn)
        
        #print(stock)
        
        return stock



    # old ==================================================
    def IndicatorContentRead(self):
        print("IndicatorContentRead")
        # 建立Connection物件
        conn = pymysql.connect(**db_homeTaibonniiSettings157)
        # 建立Cursor物件
        #with conn.cursor() as cursor:
            # 新增資料指令
        #    command = "SELECT * FROM IndicatorContent;"
            # 執行指令
        #    cursor.execute(command)
            # 取得所有資料
        #    result = cursor.fetchall()
            # 取得第一筆資料
            #result = cursor.fetchone()
        #    print(" ")
        #    print("Read", cursor.rowcount, "row(s) of data.")
        #    print(" ")
        #    print(result)
        #    print(" ")
        
        stock = pd.read_sql('SELECT * FROM IndicatorContent;', con = conn)
        
        #print(stock)
        
        #cursor.close()
        #conn.close()
        
        return stock




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

class MysqlJourneysgoStore():
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
            #print("MysqlStore__init->self.conn", self.conn)
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




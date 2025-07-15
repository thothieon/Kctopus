#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

from flask import Flask, request, render_template, send_file
from flask_cors import CORS
#from gevent import pywsgi

from mysqlTestStore import MysqlTestStore
from mysqliDivingStore import MysqliDivingStore
from mysqlJourneysgoStore import MysqlJourneysgoStore

from moduleMysqliDivingStore import ModuleMysqliDivingStore
from moduleMysqlLineAPI import ModuleMysqlLineMAPI
from moduleLineAPI import ModuleLineAPI
from moduleLineNOTifyAPI import ModuleLineNotifyAPI


app = Flask(__name__, static_folder="static", static_url_path="/")
CORS(app)

mysqlName = "hometest"

########## Test Black ##################################################
@app.route("/")
def routeMain():
    print("routeMain")
    return "<h1>Hello , This a Restful Api Server by Flask...</h1>"
    
@app.route("/test01")
def test01():
    print("test01_init")
    
    machineGroup='idiving'
    mysqlName='idiving'
    
    mainMysqlStore = ModuleMysqliDivingStore(machineGroup, mysqlName)
    maintmp = mainMysqlStore.mysqlTest01()
    print("linetest01_maintmp-> " + maintmp)
    
    return "<h1>test01, This a Restful Api Server by Flask...</h1>"
    
@app.route("/linetest")
def linetest():
    print("linetest_init")
    
    machineGroup='idiving'
    mysqlName='idiving'
    
    mainMysqlStore = ModuleMysqlLineMAPI(machineGroup, mysqlName)
    maintmp = mainMysqlStore.mysqlTest01()
    print("linetest_maintmp-> " + maintmp)
    
    ModuleLineNotifyAPI.lineNotifyMessageTest('fghfghfg')
    
    return "<h1>linetest, This a Restful Api Server by Flask...</h1>"
    
@app.route("/linetest01")
def linetest01():
    print("linetest01_init")
    
    machineGroup='idiving'
    mysqlName='idiving'
    
    mainMysqlStore = ModuleMysqlLineMAPI(machineGroup, mysqlName)
    maintmp = mainMysqlStore.mysqlTest01()
    print("linetest01_maintmp-> " + maintmp)
    
    ModuleLineAPI.lineMessageTest01()
    
    return "<h1>linetest01, This a Restful Api Server by Flask...</h1>"
    
@app.route("/htmltest")
def htmltest():
    print("htmltest_init")
    
    # 當使用者以 GET 方法訪問該路徑時，request.args 會將 URL 中的參數以 tuple 格式讀取
    # 使用 get() 方法獲取 'name' 參數的值，如果參數不存在則返回 None
    name = request.args.get('name')
    
    # 自動讀取 static/images 資料夾中的所有圖片檔案
    image_folder = os.path.join(app.static_folder, "images")
    images = [f for f in os.listdir(image_folder) if f.endswith((".jpg", ".png", ".jpeg", ".gif"))]
    
    # 將 name 參數傳遞給模板以供顯示
    #return render_template('htmltest.html', name=name)
    return render_template('0101-0331/01010331_9.docx.html', name=name)
    #return "<h1>htmltest_init, This a Restful Api Server by Flask...</h1>>"


    
########## Journeysgo Black ##################################################

########## iDiving Black ##################################################


########## Main Black ##################################################
@app.route("/idivingtestupdata", methods=['POST'])
def idivingtestupdata():
    print("idivingtestupdata")
    
    # 從 JSON 資料中取得資料
    data = request.json
    name = data.get('name')
    email = data.get('email')
    print('data -> ' + str(data))
    
    mysqlName = 'idiving'
    machineGroup = 'idiving'
    
    mainMysqlStore = MysqliDivingStore(machineGroup, mysqlName)
    maintmp = mainMysqlStore.mysqlTest01()
    print("idivingtestupdata_maintmp -> " + maintmp)
    
    return "<h1>idivingtestupdata , This a Restful Api Server by Flask...</h1>"

if __name__ == "__main__":
    print(" ")
    port = int(os.environ.get('PORT', 5836))
    #print("port : " + str(port))
    app.run(host='0.0.0.0', port=port, debug=True)
    #server = pywsgi.WSGIServer( ('0.0.0.0', 8336 ), app )
    #server.serve_forever()
    #
    #app.run(host='0.0.0.0', port=port,debug=True)
    
    
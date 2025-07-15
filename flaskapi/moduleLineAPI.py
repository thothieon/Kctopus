# coding=utf-8
import os
import sys
import datetime
import requests

# https://ithelp.ithome.com.tw/articles/10223413

msg = ''

# era643928
# 錢錢 era643928 提醒
tokenMoney = 'Yu3HySgSUJGI43uJnGH4nxDCGahOHEndVsUAabBa7gZ'

# 出團小幫手群組
tokenTest = 'FIGXSo5MEA1RJ23q7vLN5WuhkkYcdDp6JsjNmfyWvn7'


class ModuleLineAPI():
    # line Message Test ==================================================
    def lineMessageTest(msg):
        headers = {
            "Authorization": "Bearer " + tokenTest,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {'message': msg}
        r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
        return r.status_code
        
    def lineMessageTest01():
        print("lineMessageTest01")
        return 'lineMessageTest01'


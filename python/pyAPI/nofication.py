from win10toast import ToastNotifier
import requests
import json
import time


def update():
    r=requests.get('https://coronavirus-19-api.herokuapp.com/all') 
    data=r.json()
    text=f'Số ca nhiễm: {data["cases"]}\n Số ca tử vong: {data["deaths"]}\n Số ca hồi phục: {data["recovered"]}'

    while True:#python hỗ trợ build file này

        t=ToastNotifier()
        t.show_toast("Covid 19 analytics - by Khanh@@",text,duration=6)
        time.sleep(10)# 10s sẽ báo 1 lần/ cai nay ma chay exe thi hay

update()

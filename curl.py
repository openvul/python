#!/bin/env python
import requests
import json
import time
import sys

def get_http(url,timeout,flag):
    headers = {
    'User-Agent': 'Chrome/70.0.1453.110',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest'
    }
    try:
	cookies = {"PHPSESSID":"rg74r9hg0recu4df6akhhipdh4"}
        s = requests.session()
        # s.proxies = {'http':'118.114.77.47:8080'}
        r = s.get(url,headers=headers,timeout=timeout,cookies=cookies,verify=False)
        r.encoding = 'utf-8'
        print('status:' + str(r.status_code))
        if flag:
            # print('X-Powered-By:' + r.headers['X-Powered-By']),
            print('Server:' + r.headers['Server'])
        else:
            print(r.text)
    except requests.RequestException as e:
        print(e)
    except Exception as e:
        print(format(e))

def post_http(url,sec):
    headers = {
    'User-Agent': 'curl/7.99.0'
    }
    payload = {
    'key1': 'value1',
    'key2': 'value2'
    }
    r = requests.post(url,headers=headers,data=payload,timeout=sec,verify=False)
    print(r.text)

def post_json_http(url,sec):
    headers = {
    'content-type': 'application/json',
    'X-Forwarded-For':'127.0.0.1',
    'User-Agent': 'curl/7.99.0'
    }
    payload = json.dumps({
    'username': 'admin',
    'password': '21232f297a57a5a743894a0e4a801fc3'
    })
    s = requests.session()
    s.proxies = {'http':'118.114.77.47:8080'}
    r = s.post(url,headers=headers,data=payload,timeout=sec,verify=False)
    print(r.text)

# post_json_http("http://aiezu.com/test.php",10)
# while True:
#     get_http('http://ip.cn',5,0)
#     time.sleep(2)

# for i in range(1,3):
#     print i,
#
if(len(sys.argv) < 2):
	print("Usage: python curl.py http://www.baidu.com")
	exit(1)

url = sys.argv[1]
print url
get_http(url,10,True)

# -*- coding: utf-8 -*-

import requests
import json
import time
import urllib3
# import sys
# # reload(sys)
# sys.setdefaultencoding('utf-8')

def login(domain,username,password):
    """
    模拟用户登陆，得到cookie
    :param domain:企业域
    :param username: 账号
    :param password: 密码
    :return: cookie值
    """
    body_string = "domain="+domain+"&username="+username+"&password="+password+"&_xsrf="
    header = {'Host': 'www.bdp.cn',
              'Connection': 'keep-alive',
              'Content-Length': '56',
              'Sec-Fetch-Mode': 'cors',
              'Origin': 'https://www.bdp.cn',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
              'Content-Type': 'application/x-www-form-urlencoded',
              'Accept': '*/*',
              'Sec-Fetch-Site': 'same-origin',
              'Referer': 'https://www.bdp.cn/login.html?lang=zh',
              'Accept-Encoding': 'gzip, deflate, br',
              'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
              }
    r = requests.post("https://www.bdp.cn/api/user/login", headers=header, data=body_string)
    response_body = json.loads(r.text)
    if(response_body['status']!='0'):
        print('模拟登陆失败，失败信息:'+response_body['errstr'])
        print('登陆接口返回Response_Body：' + json.dumps(response_body, ensure_ascii=False))
        print('登陆接口返回Response_Header: ' + str(r.headers))
        return None
    else:
        set_cookie = r.headers.get('Set-Cookie')
        import re
        array = re.split('[;,]', set_cookie)
        cookieValue = ''
        for arr in array:
            if arr.find('token') >= 0 or arr.find("theme_id") >= 0 or arr.find("user_id") >= 0:
                cookieValue += arr + ';'
        print("模拟登陆成功，得到cookie为 "+cookieValue[:-1])
        return cookieValue[:-1]


def delete_tb(cookie,tb_id):
    """
    模拟已登陆的用户，删除合表
    :param cookie: 上面模拟登陆拿到的cookie
    :param tb_id: 将要删除的表id
    :return:
    """
    header={'Host': 'www.bdp.cn',
    'Connection': 'keep-alive',
    'Content-Length':'58',
    'Sec-Fetch-Mode': 'cors',
    'Origin': 'https://www.bdp.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://www.bdp.cn/login.html?lang=zh',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': cookie
    }
    time_stamp = (str(time.time()).replace('.','')[0:13])
    body_string = '_t='+time_stamp+'&tb_id='+tb_id
    r=requests.post("https://www.bdp.cn/api/tb/delete",headers=header,data=body_string,verify=False)
    response_json = json.loads(r.text)

    if response_json.get('status')!='0':
        print("id:"+tb_id+" 删表失败,失败信息:"+response_json.get('errstr'))
        print('删表接口返回Response_Body：' + json.dumps(response_json, ensure_ascii=False))
        print("删表接口返回Response_Header: " + str(r.headers))
    else:
        print("id:"+tb_id+" 删表成功")


cookie = login(domain='cmbsz',username='admin',password='cmbsz@2016') # 拿到cookie
tb_id = 'tb_9d0becebe1bf416b92ab88623133342c'  # 填入要删除的表id
if cookie is not None:  # 登陆成功的话（cookie不为空），进行删表操作
    delete_tb(cookie=cookie, tb_id=tb_id)




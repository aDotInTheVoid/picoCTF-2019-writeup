from os import environ
from pwn import *

EXEC = "/problems/practice-run-1_0_62b61488e896645ebff9b6c97d0e775e/run_this"
s = ssh(
    host="2019shell1.picoctf.com",
    user=environ["PICOUSER"],
    password=environ["PICOPSWD"],
)

sh = s.process(EXEC)

x = sh.recvrepeat()

print(x.decode(errors="ignore"))

s.close()

from pwn import *

# DIR="/problems/time-s-up_6_480d53541469436212e30dad5b4ce691"
DIR = "."
p = process(DIR + "/times-up")

rawin = p.recv()
math = rawin[len("Challenge: ") : rawin.index(b"\n")]
p.sendline(str(eval(math)))

p.recv()
print(p.recv())

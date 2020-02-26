# practice-run-1
The easy way is to conect with ssh
```shell
yeswriteup@pico-2019-shell1:~$ cd /problems/practice-run-1_0_62b61488e896645ebff9b6c97d0e775e
yeswriteup@pico-2019-shell1:/problems/practice-run-1_0_62b61488e896645ebff9b6c97d0e775e$ ls
run_this
yeswriteup@pico-2019-shell1:/problems/practice-run-1_0_62b61488e896645ebff9b6c97d0e775e$ ./run_this
picoCTF{g3t_r3adY_2_r3v3r53}
```
Or use pwntools
```python

from os import environ
from pwn import *

EXEC='/problems/practice-run-1_0_62b61488e896645ebff9b6c97d0e775e/run_this'
s = ssh(host='2019shell1.picoctf.com',
        user=environ["PICOUSER"],
        password=environ["PICOPSWD"])

sh = s.process(EXEC)

x = sh.recvrepeat()

print(x.decode(errors='ignore'))

s.close()
```
flag: `picoCTF{g3t_r3adY_2_r3v3r53}`
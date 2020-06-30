# Time's Up

We need to go quickly.

```python
from pwn import *

DIR="/problems/time-s-up_6_480d53541469436212e30dad5b4ce691"
#DIR = "."
p = process(DIR + "/times-up")

rawin = p.recv()
math = rawin[len("Challenge: ") : rawin.index(b"\n")]
p.sendline(str(eval(math)))

p.recv()
print(p.recv())
```
This will get the question, solve it, and print the flag. It needs to be executed on the server, as it is time sensitive,

Place the code in the home dir, but it needs to be run from the problem dir, or the executable cant find the flag

```
yeswriteup@pico-2019-shell1:~$ cd /problems/time-s-up_6_480d53541469436212e30dad5b4ce691
yeswriteup@pico-2019-shell1:/problems/time-s-up_6_480d53541469436212e30dad5b4ce691$ python ~/solve.py
[+] Starting local process '/problems/time-s-up_6_480d53541469436212e30dad5b4ce691/times-up': pid 2341595
picoCTF{Gotta go fast. Gotta go FAST. #1626a7fb}

[*] Process '/problems/time-s-up_6_480d53541469436212e30dad5b4ce691/times-up' stopped with exit code 0 (pid 2341595)
yeswriteup@pico-2019-shell1:/problems/time-s-up_6_480d53541469436212e30dad5b4ce691$
```

Flag: `picoCTF{Gotta go fast. Gotta go FAST. #1626a7fb}`
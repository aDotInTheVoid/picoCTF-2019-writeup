# Based
Here is a script that will solve it [1]. Realisticly you would do it with googleing,
but I want to say something else. [pwntools](https://github.com/Gallopsled/pwntools)
is a very usefull python package for this. Make sure you have it.

```python
from pwn import *

sh = remote('2019shell1.picoctf.com', 44303)

binary_data = sh.recvuntil('Input:\n').decode().split('\n')[2].split(' ')[3:-3]
binary_data = ''.join(map(lambda x: chr(int(x, 2)), binary_data))
sh.sendline(binary_data)

oct_data = sh.recvuntil('Input:\n').decode().split('\n')[0].split('the  ')[-1].split(' as')[0].split(' ')
oct_data = ''.join(map(lambda x: chr(int(x, 8)), oct_data))
sh.sendline(oct_data)

hex_data = sh.recvuntil('Input:\n').decode().split('\n')[0].split('the ')[-1].split(' as')[0]
hex_data = bytearray.fromhex(hex_data).decode()
sh.sendline(hex_data)

sh.interactive()
```

flag: `picoCTF{learning_about_converting_values_b515dfd2}`

***

1. Script adapted to python3 from [Alan Chang's](https://tcode2k16.github.io/blog/) [exelent writeup](https://tcode2k16.github.io/blog/posts/picoctf-2019-writeup/general-skills/#based)
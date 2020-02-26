# Investigative Reversing 1
Each png has extra data. The binary is also linux
```bash
$pngcheck *.png
mystery.png  additional data after IEND chunk
ERROR: mystery.png
mystery2.png  additional data after IEND chunk
ERROR: mystery2.png
mystery3.png  additional data after IEND chunk
ERROR: mystery3.png

Errors were detected in 3 of the 3 files tested.
$file mystery
mystery: ELF 64-bit LSB shared object x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/l, for GNU/Linux 3.2.0, BuildID[sha1]=1b08f7a782a77a6eeb80d7c1d621b4f16f76200a, not stripped
```
Again we open the binary in ghidra, and after some renaming we get
```cpp
void main(void)

{
  FILE *flag_file;
  FILE *mistery;
  FILE *mistery2;
  FILE *mistery3;
  long in_FS_OFFSET;
  char flag3;
  int i1;
  int i2;
  int i3;
  char flag [4];
  char flag5;
  char flag6;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  flag_file = fopen("flag.txt","r");
  mistery = fopen("mystery.png","a");
  mistery2 = fopen("mystery2.png","a");
  mistery3 = fopen("mystery3.png","a");
  if (flag_file == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (mistery == (FILE *)0x0) {
    puts("mystery.png is missing, please run this on the server");
  }
  fread(flag,0x1a,1,flag_file);
  fputc((int)flag[1],mistery3);
  fputc((int)(char)(flag[0] + '\x15'),mistery2);
  fputc((int)flag[2],mistery3);
  flag3 = flag[3];
  fputc((int)flag6,mistery3);
  fputc((int)flag5,mistery);
  i1 = 6;
  while (i1 < 10) {
    flag3 = flag3 + '\x01';
    fputc((int)flag[(long)i1],mistery);
    i1 = i1 + 1;
  }
  fputc((int)flag3,mistery2);
  i2 = 10;
  while (i2 < 0xf) {
    fputc((int)flag[(long)i2],mistery3);
    i2 = i2 + 1;
  }
  i3 = 0xf;
  while (i3 < 0x1a) {
    fputc((int)flag[(long)i3],mistery);
    i3 = i3 + 1;
  }
  fclose(mistery);
  fclose(flag_file);
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```
Now we need to pull the extra bits out of each image. 

- mystery.png: `43 467b 416e 315f 3337 6432 3466 6664 7d`
- mystery3.png: `8573`
- mystery3.png: `696354307468615f`

```python
from pwn import *
m1 = unhex('43 467b 416e 315f 3337 6432 3466 6664 7d'.replace(' ', ''))
m2 = unhex('8573')
m3 = unhex('696354307468615f')

# 0x1a from 2nd fread arg 
flag = bytearray("0"*0x1a, 'ascii')

flag[1] = m3[0]
flag[0] = m2[0] - 0x15
flag[2] = m3[1]
flag[4] = m1[0]
flag[5] = m3[2]

for i in range(6,10):
  flag[i] = m1[i-5] # The minus five comes from the fact that it's being pushed to the end

for i in range(10, 15):
  flag[i] = m3[i-7]

for i in range(15,26):
  flag[i] = m1[i-10]
```
we haven't delt with `flag3` but we can guess from context it will be `o`
```python
flag[3] = ord('o')
```
flag: `picoCTF{An0tha_1_37d24ffd}`

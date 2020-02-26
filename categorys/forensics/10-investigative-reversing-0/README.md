# Investigative Reversing 0
After downloading, the first thing to do is run `file`
```bash
$file mystery*
mystery:     ELF 64-bit LSB shared object x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/l, for GNU/Linux 3.2.0, BuildID[sha1]=34b772a4f30594e2f30ac431c72667c3e10fa3e9, not stripped
mystery.png: PNG image data, 1411 x 648, 8-bit/color RGB, non-interlaced
```
Next we decompile the binary with [ghidra](https://ghidra-sre.org/). Learn how to use it because it's super usefull.

```cpp
void main(void)

{
  long lVar1;
  FILE *flag_file;
  FILE *png_file;
  size_t sucess;
  long in_FS_OFFSET;
  int i;
  int j;
  char flag4 [4];
  char flag5;
  char flag6;
  char local_29;
  
  lVar1 = *(long *)(in_FS_OFFSET + 0x28);
  flag_file = fopen("flag.txt","r");
  png_file = fopen("mystery.png","a");
  if (flag_file == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (png_file == (FILE *)0x0) {
    puts("mystery.png is missing, please run this on the server");
  }
  sucess = fread(flag4,0x1a,1,flag_file);
  if ((int)sucess < 1) {
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("at insert");
  fputc((int)flag4[0],png_file);
  fputc((int)flag4[1],png_file);
  fputc((int)flag4[2],png_file);
  fputc((int)flag4[3],png_file);
  fputc((int)flag5,png_file);
  fputc((int)flag6,png_file);
  i = 6;
  while (i < 0xf) {
    fputc((int)(char)(flag4[(long)i] + '\x05'),png_file);
    i = i + 1;
  }
  fputc((int)(char)(local_29 + -3),png_file);
  j = 0x10;
  while (j < 0x1a) {
    fputc((int)flag4[(long)j],png_file);
    j = j + 1;
  }
  fclose(png_file);
  fclose(flag_file);
  if (lVar1 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```
Essensialy it has taken the flag and dumpt it into the png. This is confirmed by 
the fact that pngcheck shows extra data.
```bash
$pngcheck mystery.png 
mystery.png  additional data after IEND chunk
ERROR: mystery.png
$xxd mystery.png | tail
0001e7f0: 8220 0882 2008 8220 0882 2064 1f32 1221  . .. .. .. d.2.!
0001e800: 0882 2008 8220 0882 2008 42f6 2123 1182  .. .. .. .B.!#..
0001e810: 2008 8220 0882 2008 8220 641f 3212 2108   .. .. .. d.2.!.
0001e820: 8220 0882 2008 8220 0842 f621 2311 8220  . .. .. .B.!#.. 
0001e830: 0882 2008 8220 0882 2064 1f32 1221 0882  .. .. .. d.2.!..
0001e840: 2008 8220 0882 2008 42f6 2123 1182 2008   .. .. .B.!#.. .
0001e850: 8220 0882 2008 8220 6417 ffef fffd 7f5e  . .. .. d......^
0001e860: ed5a 9d38 d01f 5600 0000 0049 454e 44ae  .Z.8..V....IEND.
0001e870: 4260 8270 6963 6f43 544b 806b 357a 7369  B`.picoCTK.k5zsi
0001e880: 6436 715f 6134 3736 6630 3662 7d         d6q_a476f06b}
```
After the IEND their are 4 bytes of crc, and then the data:
`70 6963 6f43 544b 806b 357a 7369 6436 715f 6134 3736 6630 3662 7d`

Now we can undo the script and get the flag.
```python
bits = '70 69 63 6f 43 54 4b 80 6b 35 7a 73 69 64 36 71 5f 61 34 37 36 66 30 36 62 7d'.split()
bits = list(map(lambda x: int(x, 16), bits))
for i in range(6, 15):
  bits[i] -= 5


print(''.join(map(chr, bits)))
```
This  gives `picoCTF{f0und_1q_a476f06b}` but doesnt acount for `fputc((int)(char)(local_29 + -3),png_file);` We don't know the charecter at index 15 (the `q`). We can guess that it would be a `t` and this is right
```python
bits = '70 69 63 6f 43 54 4b 80 6b 35 7a 73 69 64 36 71 5f 61 34 37 36 66 30 36 62 7d'.split()
bits = list(map(lambda x: int(x, 16), bits))
for i in range(6, 15):
  bits[i] -= 5

bits[15] = ord("t")

print(''.join(map(chr, bits)))
```
flag: `picoCTF{f0und_1t_a476f06b}`
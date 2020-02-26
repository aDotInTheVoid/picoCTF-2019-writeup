# Investigative Reversing 2
This time the image is a `bmp` not a `png`. Again we run the binary through ghidra.
After noodling throught the variables we get this
```cpp

undefined8 main(void)

{
  FILE *flag_stream_1;
  FILE *orig_bmp;
  FILE *encoded_bmp;
  size_t has_read;
  size_t sVar1;
  size_t has_read_3;
  ulong mutated_flag_chr;
  size_t has_read_2;
  long in_FS_OFFSET;
  byte orig_chr;
  int is_more;
  int k;
  int i;
  int j;
  FILE *flag_file;
  char flag [56];
  long canary;
  long canary2;
  
  canary2 = *(long *)(in_FS_OFFSET + 0x28);
  flag_stream_1 = fopen("flag.txt","r");
  orig_bmp = fopen("original.bmp","r");
  encoded_bmp = fopen("encoded.bmp","a");
  if (flag_stream_1 == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (orig_bmp == (FILE *)0x0) {
    puts("original.bmp is missing, please run this on the server");
  }
  has_read = fread(&orig_chr,1,1,orig_bmp);
  is_more = (int)has_read;
  k = 0;
  while (k < 2000) {
    fputc((int)(char)orig_chr,encoded_bmp);
    sVar1 = fread(&orig_chr,1,1,orig_bmp);
    is_more = (int)sVar1;
    k = k + 1;
  }
  has_read_3 = fread(flag,0x32,1,flag_stream_1);
  if ((int)has_read_3 < 1) {
    puts("flag is not 50 chars");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  i = 0;
  while (i < 0x32) {
    j = 0;
    while (j < 8) {
      mutated_flag_chr = codedChar(j,flag[(long)i] - 5,orig_chr);
      fputc((int)(char)mutated_flag_chr,encoded_bmp);
      fread(&orig_chr,1,1,orig_bmp);
      j = j + 1;
    }
    i = i + 1;
  }
  while (is_more == 1) {
    fputc((int)(char)orig_chr,encoded_bmp);
    has_read_2 = fread(&orig_chr,1,1,orig_bmp);
    is_more = (int)has_read_2;
  }
  fclose(encoded_bmp);
  fclose(orig_bmp);
  fclose(flag_stream_1);
  if (canary2 == *(long *)(in_FS_OFFSET + 0x28)) {
    return 0;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}
```
Essensialy we go over 2000+/-1 charecters, copying. Then we add the flag in some way, then we go over the rest of the charecters, also copying. We also use a auxilary function `codedChar` to do some of the mangling. Looking at it in ghidra, we can get 
```cpp

ulong codedChar(int cyclic_idx,byte flag_chr,byte orig_chr)

{
  byte shifted;
  
  shifted = flag_chr;
  if (cyclic_idx != 0) {
    shifted = (byte)((int)(char)flag_chr >> ((byte)cyclic_idx & 0x1f));
  }
  return (ulong)(orig_chr & 0xfe | shifted & 1);
}
```
However when `cyclic_idx==0` we can pretend the shift will still run as a shift by zero preserves the variable, so i think the branch was itnroduced by gcc as an optimisation.

Therefor the python to decode it looks like
```python
with open('./encoded.bmp', 'rb') as f:
  bits = f.read()

fbits = bits[2000:2000+(50*8)]
out=''

for i in range(0x32):
    for j in range(8):
```
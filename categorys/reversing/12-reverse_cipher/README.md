# reverse_cipher
Acording to r2, the asm is 
```x86asm
            ; DATA XREF from entry0 @ 0x10bd
┌ 324: int main (int argc, char **argv, char **envp);
│           ; var void *ptr @ rbp-0x50
│           ; var int64_t var_39h @ rbp-0x39
│           ; var size_t var_24h @ rbp-0x24
│           ; var file*var_20h @ rbp-0x20
│           ; var file*stream @ rbp-0x18
│           ; var signed int64_t var_ch @ rbp-0xc
│           ; var signed int64_t var_8h @ rbp-0x8
│           ; var int64_t c @ rbp-0x1
│           0x00001185      55             push rbp
│           0x00001186      4889e5         mov rbp, rsp
│           0x00001189      4883ec50       sub rsp, 0x50
│           0x0000118d      488d35740e00.  lea rsi, [0x00002008]       ; "r" ; const char *mode
│           0x00001194      488d3d6f0e00.  lea rdi, str.flag.txt       ; 0x200a ; "flag.txt" ; const char *filename
│           0x0000119b      e8d0feffff     call sym.imp.fopen          ; file*fopen(const char *filename, const char *mode)
│           0x000011a0      488945e8       mov qword [stream], rax
│           0x000011a4      488d35680e00.  lea rsi, [0x00002013]       ; "a" ; const char *mode
│           0x000011ab      488d3d630e00.  lea rdi, str.rev_this       ; 0x2015 ; "rev_this" ; const char *filename
│           0x000011b2      e8b9feffff     call sym.imp.fopen          ; file*fopen(const char *filename, const char *mode)
│           0x000011b7      488945e0       mov qword [var_20h], rax
│           0x000011bb      48837de800     cmp qword [stream], 0
│       ┌─< 0x000011c0      750c           jne 0x11ce
│       │   0x000011c2      488d3d570e00.  lea rdi, str.No_flag_found__please_make_sure_this_is_run_on_the_server ; 0x2020 ; "No flag found, please make sure this is run on the server" ; const char *s
│       │   0x000011c9      e862feffff     call sym.imp.puts           ; int puts(const char *s)
│       │   ; CODE XREF from main @ 0x11c0
│       └─> 0x000011ce      48837de000     cmp qword [var_20h], 0
│       ┌─< 0x000011d3      750c           jne 0x11e1
│       │   0x000011d5      488d3d7e0e00.  lea rdi, str.please_run_this_on_the_server ; 0x205a ; "please run this on the server" ; const char *s
│       │   0x000011dc      e84ffeffff     call sym.imp.puts           ; int puts(const char *s)
│       │   ; CODE XREF from main @ 0x11d3
│       └─> 0x000011e1      488b55e8       mov rdx, qword [stream]
│           0x000011e5      488d45b0       lea rax, [ptr]
│           0x000011e9      4889d1         mov rcx, rdx                ; FILE *stream
│           0x000011ec      ba01000000     mov edx, 1                  ; size_t nmemb
│           0x000011f1      be18000000     mov esi, 0x18               ; size_t size
│           0x000011f6      4889c7         mov rdi, rax                ; void *ptr
│           0x000011f9      e842feffff     call sym.imp.fread          ; size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream)
│           0x000011fe      8945dc         mov dword [var_24h], eax
│           0x00001201      837ddc00       cmp dword [var_24h], 0
│       ┌─< 0x00001205      7f0a           jg 0x1211
│       │   0x00001207      bf00000000     mov edi, 0                  ; int status
│       │   0x0000120c      e86ffeffff     call sym.imp.exit           ; void exit(int status)
│       │   ; CODE XREF from main @ 0x1205
│       └─> 0x00001211      c745f8000000.  mov dword [var_8h], 0
│       ┌─< 0x00001218      eb23           jmp 0x123d
│       │   ; CODE XREF from main @ 0x1241
│      ┌──> 0x0000121a      8b45f8         mov eax, dword [var_8h]
│      ╎│   0x0000121d      4898           cdqe
│      ╎│   0x0000121f      0fb64405b0     movzx eax, byte [rbp + rax - 0x50]
│      ╎│   0x00001224      8845ff         mov byte [c], al
│      ╎│   0x00001227      0fbe45ff       movsx eax, byte [c]
│      ╎│   0x0000122b      488b55e0       mov rdx, qword [var_20h]
│      ╎│   0x0000122f      4889d6         mov rsi, rdx                ; FILE *stream
│      ╎│   0x00001232      89c7           mov edi, eax                ; int c
│      ╎│   0x00001234      e827feffff     call sym.imp.fputc          ; int fputc(int c, FILE *stream)
│      ╎│   0x00001239      8345f801       add dword [var_8h], 1
│      ╎│   ; CODE XREF from main @ 0x1218
│      ╎└─> 0x0000123d      837df807       cmp dword [var_8h], 7
│      └──< 0x00001241      7ed7           jle 0x121a
│           0x00001243      c745f4080000.  mov dword [var_ch], 8
│       ┌─< 0x0000124a      eb43           jmp 0x128f
│       │   ; CODE XREF from main @ 0x1293
│      ┌──> 0x0000124c      8b45f4         mov eax, dword [var_ch]
│      ╎│   0x0000124f      4898           cdqe
│      ╎│   0x00001251      0fb64405b0     movzx eax, byte [rbp + rax - 0x50]
│      ╎│   0x00001256      8845ff         mov byte [c], al
│      ╎│   0x00001259      8b45f4         mov eax, dword [var_ch]
│      ╎│   0x0000125c      83e001         and eax, 1
│      ╎│   0x0000125f      85c0           test eax, eax
│     ┌───< 0x00001261      750c           jne 0x126f
│     │╎│   0x00001263      0fb645ff       movzx eax, byte [c]
│     │╎│   0x00001267      83c005         add eax, 5
│     │╎│   0x0000126a      8845ff         mov byte [c], al
│    ┌────< 0x0000126d      eb0a           jmp 0x1279
│    ││╎│   ; CODE XREF from main @ 0x1261
│    │└───> 0x0000126f      0fb645ff       movzx eax, byte [c]
│    │ ╎│   0x00001273      83e802         sub eax, 2
│    │ ╎│   0x00001276      8845ff         mov byte [c], al
│    │ ╎│   ; CODE XREF from main @ 0x126d
│    └────> 0x00001279      0fbe45ff       movsx eax, byte [c]
│      ╎│   0x0000127d      488b55e0       mov rdx, qword [var_20h]
│      ╎│   0x00001281      4889d6         mov rsi, rdx                ; FILE *stream
│      ╎│   0x00001284      89c7           mov edi, eax                ; int c
│      ╎│   0x00001286      e8d5fdffff     call sym.imp.fputc          ; int fputc(int c, FILE *stream)
│      ╎│   0x0000128b      8345f401       add dword [var_ch], 1
│      ╎│   ; CODE XREF from main @ 0x124a
│      ╎└─> 0x0000128f      837df416       cmp dword [var_ch], 0x16
│      └──< 0x00001293      7eb7           jle 0x124c
│           0x00001295      0fb645c7       movzx eax, byte [var_39h]
│           0x00001299      8845ff         mov byte [c], al
│           0x0000129c      0fbe45ff       movsx eax, byte [c]
│           0x000012a0      488b55e0       mov rdx, qword [var_20h]
│           0x000012a4      4889d6         mov rsi, rdx                ; FILE *stream
│           0x000012a7      89c7           mov edi, eax                ; int c
│           0x000012a9      e8b2fdffff     call sym.imp.fputc          ; int fputc(int c, FILE *stream)
│           0x000012ae      488b45e0       mov rax, qword [var_20h]
│           0x000012b2      4889c7         mov rdi, rax                ; FILE *stream
│           0x000012b5      e896fdffff     call sym.imp.fclose         ; int fclose(FILE *stream)
│           0x000012ba      488b45e8       mov rax, qword [stream]
│           0x000012be      4889c7         mov rdi, rax                ; FILE *stream
│           0x000012c1      e88afdffff     call sym.imp.fclose         ; int fclose(FILE *stream)
│           0x000012c6      90             nop
│           0x000012c7      c9             leave
└           0x000012c8      c3             ret
```

Therefor we need to fire up [ghidra](https://ghidra-sre.org/)

```c
/* DISPLAY WARNING: Type casts are NOT being printed */

void main(void)

{
  size_t sVar1;
  char local_58 [23];
  char local_41;
  int local_2c;
  FILE *local_28;
  FILE *local_20;
  uint local_14;
  int local_10;
  char local_9;
  
  local_20 = fopen("flag.txt","r");
  local_28 = fopen("rev_this","a");
  if (local_20 == NULL) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (local_28 == NULL) {
    puts("please run this on the server");
  }
  sVar1 = fread(local_58,24,1,local_20);
  local_2c = sVar1;
  if (sVar1 < 1) {
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  local_10 = 0;
  while (local_10 < 8) {
    local_9 = local_58[local_10];
    fputc(local_9,local_28);
    local_10 = local_10 + 1;
  }
  local_14 = 8;
  while (local_14 < 23) {
    if ((local_14 & 1) == 0) {
      local_9 = local_58[local_14] + '\x05';
    }
    else {
      local_9 = local_58[local_14] + -2;
    }
    fputc(local_9,local_28);
    local_14 = local_14 + 1;
  }
  local_9 = local_41;
  fputc(local_41,local_28);
  fclose(local_28);
  fclose(local_20);
  return;
}
```

After some renaming we get

```c
void main(void)

{
  size_t result;
  char buf [23];
  char local_41;
  int local_2c;
  FILE *output;
  FILE *flag_file;
  uint j;
  int i;
  char chr;
  
  flag_file = fopen("flag.txt","r");
  output = fopen("rev_this","a");
  if (flag_file == NULL) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (output == NULL) {
    puts("please run this on the server");
  }
  result = fread(buf,24,1,flag_file);
  local_2c = result;
  if (result < 1) {
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  i = 0;
  while (i < 8) {
    chr = buf[i];
    fputc(chr,output);
    i = i + 1;
  }
  j = 8;
  while (j < 23) {
    if ((j & 1) == 0) {
      chr = buf[j] + '\x05';
    }
    else {
      chr = buf[j] + -2;
    }
    fputc(chr,output);
    j = j + 1;
  }
  chr = local_41;
  fputc(local_41,output);
  fclose(output);
  fclose(flag_file);
  return;
}
```
The important bit is here
```c
  i = 0;
  while (i < 8) {
    chr = buf[i];
    fputc(chr,output);
    i = i + 1;
  }
  j = 8;
  while (j < 23) {
    if ((j & 1) == 0) {
      chr = buf[j] + '\x05';
    }
    else {
      chr = buf[j] + -2;
    }
    fputc(chr,output);
    j = j + 1;
  }
```

Slaping together some python.
```python
inp = "picoCTF{w1{1wq83k055j5f}"
out = []

for i in range(8):
    out.append(inp[i])

for j in range(8, 23):
    if (j & 1) == 0:
        out.append(chr(ord(inp[j])-0x5))
    else:
        out.append(chr(ord(inp[j])+2))

print(''.join(out))
```

This gives `picoCTF{r3v3rs35f207e7a`. We can guess that we need a `}` to close
it. That is probaly what `local_41` was.

Trying `picoCTF{r3v3rs35f207e7a}`, it is right.

Flag: `picoCTF{r3v3rs35f207e7a}`

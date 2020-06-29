# asm3
This time the code is
```x86asm
asm3:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax
	<+5>:	mov    ah,BYTE PTR [ebp+0xa]
	<+8>:	shl    ax,0x10
	<+12>:	sub    al,BYTE PTR [ebp+0xf]
	<+15>:	add    ah,BYTE PTR [ebp+0xe]
	<+18>:	xor    ax,WORD PTR [ebp+0x10]
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret      
```
and we are calling `asm3(0xd46c9935,0xdfe28722,0xb335450f)`

This code uses funky registers

![](https://www.cs.virginia.edu/~evans/cs216/guides/x86-registers.png)

The code also gets acceess to the stack unaligned to the arguments

The CPU is oriented arount bytes, and every address is which byte to get. 
However most values are more than 8 bits, so we split the data across multiple bytes
```
+--+--+--+--+--+--+--+--+--+--+--+--+
|A |A |A |A |B |B |B |B |C |C |C |C |
+--+--+--+--+--+--+--+--+--+--+--+--+
```

If we want to read `A`, we use the index of the start, and tell the CPU to read 32 bits,
(`DWORD`)


```
+--+--+--+--+--+--+--+--+--+--+--+--+
|A |A |A |A |B |B |B |B |C |C |C |C |
+--+--+--+--+--+--+--+--+--+--+--+--+
|           |
+------------
      |
    Read
```

However their is no reason our reads need to be aligned to our variables. We can also

```
+--+--+--+--+--+--+--+--+--+--+--+--+
|A |A |A |A |B |B |B |B |C |C |C |C |
+--+--+--+--+--+--+--+--+--+--+--+--+
      |           |
      +------------
            |
          Read
```
Here we get the last 2 bytes of `A` and the first 2 bytes of `B`.

With that out of the way, how does our stack look

```
0xb335450f     <- ebp - 0x10
0xdfe28722     <- ebp - 0xc
0xd46c9935     <- ebp - 0x8
Return Address <- ebp - 0x4
Old EBP        <- ebp 
```

This is all quite gnarly, and as their are no label's I just want to run it.

As this is 32 bits, we will need the a 32 bit libc, which you may need to
install [^libc]

The modified asembly looks like this
```x86asm
.intel_syntax noprefix
.global asm3

asm3:
	push   ebp
	mov    ebp,esp
	xor    eax,eax
	mov    ah,BYTE PTR [ebp+0xa]
	shl    ax,0x10
	sub    al,BYTE PTR [ebp+0xf]
	add    ah,BYTE PTR [ebp+0xe]
	xor    ax,WORD PTR [ebp+0x10]
	nop
	pop    ebp
	ret    
  
```
We remove the position labels `<+...>`, and add some directives (starts with a `.`),
to make gcc use intel syntax, and export the function.

Then we write a simple c wrapper to call it

```c
#include <stdio.h>

int asm3(int a, int b, int c);

void main() {
    int result = asm3(0xd46c9935,0xdfe28722,0xb335450f);
    printf("0x%x\n", result);
}
```
We declare the function at the top, call it, and print the result.
```sh
gcc -m32 -c main.c -o main.o
gcc -m32 -c run.s -o asm.o
gcc -m32 main.o asm.o
```
Compiling we use `-m32` to enable 32 bit mode, and `-c` to disable the linker. In the final command, we run the linker to produce the executable `./a.out`.

Running it, we get `0xa72e`

<!-- TODO: debug with r2 and show what happens -->

[^libc]: `glibc-devel.i686` on fedora, `libc6-dev-i386` on debian based

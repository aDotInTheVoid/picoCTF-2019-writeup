# asm1
We are given the following asm
```x86asm
asm1:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x421
	<+10>:	jg     0x512 <asm1+37>
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x1b4
	<+19>:	jne    0x50a <asm1+29>
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0x13
	<+27>:	jmp    0x529 <asm1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0x13
	<+35>:	jmp    0x529 <asm1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0x7f7
	<+44>:	jne    0x523 <asm1+54>
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]
	<+49>:	sub    eax,0x13
	<+52>:	jmp    0x529 <asm1+60>
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0x13
	<+60>:	pop    ebp
	<+61>:	ret    
```
If we try to run it through gcc ([`gcc -m32 -c test.S -o asm.o`](https://explainshell.com/explain?cmd=+gcc+-m32+-c+test.S+-o+asm.o)) but this gives a bunch of errors due to the `<+32>` markers etc.

[Someone very clever](https://github.com/noahc3/picoctf-2019-solutions/tree/master/Reverse%20Engineering/asm1) figured out a way to run this, but that's not learning.

Instead [learn assembly](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html).

First let's look at the regesters we have

![x86 registers](https://www.cs.virginia.edu/~evans/cs216/guides/x86-registers.png)

The import ones are `esp` and `ebp`
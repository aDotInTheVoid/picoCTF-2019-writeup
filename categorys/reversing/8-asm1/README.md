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
and asked "What does asm1(0x1b4)"

If we try to run it through gcc ([`gcc -m32 -c test.S -o asm.o`](https://explainshell.com/explain?cmd=+gcc+-m32+-c+test.S+-o+asm.o)) but this gives a bunch of errors due to the `<+32>` markers etc.

[Someone very clever](https://github.com/noahc3/picoctf-2019-solutions/tree/master/Reverse%20Engineering/asm1) figured out a way to run this, but that's not learning.

Instead we shall [learn assembly](https://en.wikibooks.org/wiki/X86_Disassembly) as thats much more fun.

```x86asm
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
```
This is the [standard entry procedure](https://en.wikibooks.org/wiki/X86_Disassembly/Functions_and_Stack_Frames#Standard_Entry_Sequence)


Next we have 
```x86asm
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x421
```
Where are comparing (`cmp`) the literal value `0x421`. `DWORD PTR` means 32
bits, (don't ask), the `[...]` means get the value at the address of the inner,
and `ebp+0x8` is the first argument, as 4 bytes up is the return address, and 4
more bytes up is the first arguments, put their by the caller, as specified by
[calling
convensions](https://en.wikipedia.org/wiki/X86_calling_conventions#cdecl)

As we are told in the question, `DWORD PTR [ebp+0x8]` is `0x1b4`, which is less than `0x421`.

```x86asm
	<+10>:	jg     0x512 <asm1+37>
```
This is a [jump if greater](https://en.wikibooks.org/wiki/X86_Assembly/Control_Flow#Jump_if_Greater). However because the result of the compare was less, we dont jump, but continue.

```x86asm
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x1b4
	<+19>:	jne    0x50a <asm1+29>
```
Again we compare the argument, `0x1b4`, this time to `0x1b4`. As they are equal, we dont jump at the 
[jump if not equal](https://en.wikibooks.org/wiki/X86_Assembly/Control_Flow#Jump_if_Not_Equal).

```x86asm
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0x13
```
This time we `mov`e `0x1b4` into `eax`, the register which is the return value.

Next we `add` `0x13` to `eax`. This makes `eax` `hex(0x1b4 + 0x13)`, which is `0x1c7`

```x86asm
	<+27>:	jmp    0x529 <asm1+60>
```
Here we [unconditionaly jump](https://en.wikibooks.org/wiki/X86_Assembly/Control_Flow#Unconditional_Jumps) to `0x529`, which we are told is `<asm1+60>`

```x86asm
	<+60>:	pop    ebp
	<+61>:	ret 
```

This is the [standard exit](https://en.wikibooks.org/wiki/X86_Disassembly/Functions_and_Stack_Frames#Standard_Exit_Sequence), and by convension, `eax` is returned

Flag: `0x1c7`


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

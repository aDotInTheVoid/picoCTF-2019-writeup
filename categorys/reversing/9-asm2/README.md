# asm2

```x86asm
asm2:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0xa9
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x47a6
	<+38>:	jle    0x501 <asm2+20>
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]
	<+43>:	leave  
	<+44>:	ret    
```
This time we are calling with `asm2(0x9,0x1e)`

Arguments are put onto the stack right to left, so

- `[ebp+0x8]` is arg 1, ie `0x9`
- `[ebp+0xc]` is arg 2, ie `0x1e`.

The first thing that happens, after the entry, is 
```x86asm
	<+3>:	sub    esp,0x10
```
This removes `0x10`, ie 16 bytes from the `esp`, esensialy creating 4 slots on the stack.

The stack now looks like this

| address      | value          |
|--------------|----------------|
| `ebp + 0xc`  | `0x1e`         |
| `ebp + 0x8`  | `0x9`          |
| `ebp + 0x4`  | return address |
| `ebp`        | old ebp        |
| `ebp - 0x4`  | local, unknown |
| `ebp - 0x8`  | local, unknown |
| `ebp - 0xc`  | local, unknown |
| `ebp - 0x10` | local, unknown |

Next we start filling the locals

```x86asm
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]
```

| Address      | Value          | Regiseter | Value  |
|--------------|----------------|-----------|--------|
| `ebp + 0xc`  | `0x1e`         | `eax`     | `0x1e` |
| `ebp + 0x8`  | `0x9`          |
| `ebp + 0x4`  | return address |
| `ebp`        | old ebp        |
| `ebp - 0x4`  | local, unknown |
| `ebp - 0x8`  | local, unknown |
| `ebp - 0xc`  | local, unknown |
| `ebp - 0x10` | local, unknown |

```x86asm
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
```

| Address      | Value          | Regiseter | Value  |
|--------------|----------------|-----------|--------|
| `ebp + 0xc`  | `0x1e`         | `eax`     | `0x1e` |
| `ebp + 0x8`  | `0x9`          |
| `ebp + 0x4`  | return address |
| `ebp`        | old ebp        |
| `ebp - 0x4`  | `0x1e`         |
| `ebp - 0x8`  | local, unknown |
| `ebp - 0xc`  | local, unknown |
| `ebp - 0x10` | local, unknown |

```x86asm
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
```

| Address      | Value          | Regiseter | Value  |
|--------------|----------------|-----------|--------|
| `ebp + 0xc`  | `0x1e`         | `eax`     | `0x9`  |
| `ebp + 0x8`  | `0x9`          |
| `ebp + 0x4`  | return address |
| `ebp`        | old ebp        |
| `ebp - 0x4`  | `0x1e`         |
| `ebp - 0x8`  | local, unknown |
| `ebp - 0xc`  | local, unknown |
| `ebp - 0x10` | local, unknown |

```x86asm
    <+15>:	mov    DWORD PTR [ebp-0x8],eax
```

| Address      | Value          | Regiseter | Value  |
|--------------|----------------|-----------|--------|
| `ebp + 0xc`  | `0x1e`         | `eax`     | `0x9`  |
| `ebp + 0x8`  | `0x9`          |
| `ebp + 0x4`  | return address |
| `ebp`        | old ebp        |
| `ebp - 0x4`  | `0x1e`         |
| `ebp - 0x8`  | `0x9`          |
| `ebp - 0xc`  | local, unknown |
| `ebp - 0x10` | local, unknown |

Then we enter this loop

```x86asm
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0xa9
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x47a6
	<+38>:	jle    0x501 <asm2+20>
```

Anotating the controll flow, we get

```x86asm
	jmp    0x50c <asm2+31> →────────────┐ 
 ┌─→add    DWORD PTR [ebp-0x4],0x1      │
 │  add    DWORD PTR [ebp-0x8],0xa9     │
 │  cmp    DWORD PTR [ebp-0x8],0x47a6 ←─┘
 └─←jle    0x501 <asm2+20>
```

This is esensialy a while loop. While `[ebp-0x8]` is less than or equal to `0x47a6`, we run 

```x86asm
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0xa9
```

Initialy ``[ebp-0x8]` is `0x9`. `(0x47a6 - 0x9) / 0xa9` is 108.4, so we will run 109 times.

This will increment `[ebp-0x4]`, 109 times, so it's final value will be `0x1e + 109*0x1` which is `0x8b`

Finaly we

```x86asm
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]
	<+43>:	leave  
	<+44>:	ret   
```
This puts `[ebp-0x4]` in the return value, [`leave`](https://stackoverflow.com/a/29790275/11466826) clears up the stack, and then we return.


---

Diagrams adapted from [Dvd848](https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/asm2.md)
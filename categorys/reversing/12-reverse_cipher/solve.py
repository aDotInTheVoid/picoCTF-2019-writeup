inp = "picoCTF{w1{1wq83k055j5f}"
out = []

for i in range(8):
    out.append(inp[i])

for j in range(8, 23):
    if (j & 1) == 0:
        out.append(chr(ord(inp[j]) - 0x5))
    else:
        out.append(chr(ord(inp[j]) + 2))

print("".join(out))

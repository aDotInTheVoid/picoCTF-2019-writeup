bits = "70 69 63 6f 43 54 4b 80 6b 35 7a 73 69 64 36 71 5f 61 34 37 36 66 30 36 62 7d".split()
bits = list(map(lambda x: int(x, 16), bits))
for i in range(6, 15):
    bits[i] -= 5

bits[15] = ord("t")

print("".join(map(chr, bits)))

import itertools

KEY_LEN = 16


shifters = []
for i in range(KEY_LEN):
    shifters.append([])
expected = [
    0x89,
    0x50,
    0x4E,
    0x47,
    0x0D,
    0x0A,
    0x1A,
    0x0A,
    0x00,
    0x00,
    0x00,
    0x0D,
    0x49,
    0x48,
    0x44,
    0x52,
]
with open("bytes.txt") as f:
    bytes_arr = list(map(int, f.read().split(" ")))
    for i in range(KEY_LEN):
        for shifter in range(10):
            j = 0  # We only need to care about the first 16 bytes
            offset = (((j + shifter) * KEY_LEN) % len(bytes_arr)) + i
            if bytes_arr[offset] == expected[i]:
                shifters[i].append(shifter)

for p in itertools.product(*shifters):
    key = "".join("{}".format(n) for n in p)
    print("key could be {}".format(key))

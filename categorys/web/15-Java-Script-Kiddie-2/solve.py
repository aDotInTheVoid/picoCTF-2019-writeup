import itertools
KEY_LEN = 16

from PIL import Image
import itertools, io, os
KEY_LEN = 16

def create_png(bytes_arr, key, out_dir_path):
    result = [0] * len(bytes_arr)
    for i in range(KEY_LEN):
        shifter = int(key[i*2:i*2+1])
        for j in range(len(bytes_arr) // KEY_LEN):
            result[(j * KEY_LEN) + i] = bytes_arr[(((j + shifter) * KEY_LEN) % len(bytes_arr)) + i]
    img_bytes = io.BytesIO(bytes(result))

    try:
        img = Image.open(img_bytes)
        img.save("{}.png".format(key))
        print("key is {}".format(key))
    except IOError:
        pass

shifters = []
for i in range(KEY_LEN):
    shifters.append([])

expected = [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, 0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52]
with open("bytes.txt") as f:
    bytes_arr = list(map(int, f.read().split(" ")))
    for i in range(KEY_LEN):
        for shifter in range(10):
            j = 0
            offset = (((j + shifter) * KEY_LEN) % len(bytes_arr)) + i
            if bytes_arr[offset] == expected[i]:
                shifters[i].append(shifter)               

for p in itertools.product(*shifters):
    key = "".join("{}0".format(n) for n in p)
    create_png(bytes_arr, key, "out")
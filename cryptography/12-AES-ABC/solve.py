import math

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))


def to_bytes(n):
    s = hex(n)
    s_n = s[2:]
    if "L" in s_n:
        s_n = s_n.replace("L", "")
    if len(s_n) % 2 != 0:
        s_n = "0" + s_n
    decoded = s_n.decode("hex")
    pad = len(decoded) % BLOCK_SIZE
    if pad != 0:
        decoded = "\0" * (BLOCK_SIZE - pad) + decoded
    return decoded


def remove_line(s):
    return s[: s.index("\n") + 1], s[s.index("\n") + 1 :]


def parse_header_ppm(f):
    data = f.read()
    header = ""
    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i
    return header, data


with open("body.enc.ppm", "rb") as cf:
    hed, dat = parse_header_ppm(cf)

cb = [dat[i * BLOCK_SIZE : (i + 1) * BLOCK_SIZE] for i in range(len(dat) / BLOCK_SIZE)]
mb = []
for i in range(len(cb) - 1):
    abc_n = int(cb[i].encode("hex"), 16)
    abc_n_plus_1 = int(cb[i + 1].encode("hex"), 16)
    delta = abc_n_plus_1 - abc_n
    while delta < 0:
        delta += UMAX
    mb.append(to_bytes(delta))

with open("flag.ppm", "wb") as mf:
    mf.write(hed)
    mf.write("".join(mb))

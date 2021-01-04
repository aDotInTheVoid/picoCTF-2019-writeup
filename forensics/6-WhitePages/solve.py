from pwn import unbits

with open("./hexvals.txt", "r") as f:
    inp = f.read()

ab = inp.replace("e28083", "A").replace("20", "B")
out = ab.replace("A", "0").replace("B", "1")

print(unbits(out).decode())

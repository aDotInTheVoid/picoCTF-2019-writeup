# whats-the-difference
First download the pictures with wget
```bash
wget https://2019shell1.picoctf.com/static/473cf765877f28edf95140f90cd76b59/kitters.jpg
wget https://2019shell1.picoctf.com/static/473cf765877f28edf95140f90cd76b59/cattos.jpg
```
Then using `rb` (read binary) mode, we can use python to get the diff
```python
with open('./kitters.jpg', 'rb') as f:
  kitters = f.read()

with open('./cattos.jpg', 'rb') as f:
  cattos = f.read()

flag = ''
for i in range(min(len(kitters), len(cattos))):
  if kitters[i] != cattos[i]:
    flag += chr(cattos[i])

print(flag)
```
flag: `picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j311y_aslkjfdsalkfslkflkjdsfdszmz10548}`

***

Script adapted to python3 from [Alan Chang's](https://tcode2k16.github.io/blog/) [exelent writeup](https://tcode2k16.github.io/blog/posts/picoctf-2019-writeup/general-skills/#based)


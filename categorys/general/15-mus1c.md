# mus1c
Some awareness of programing memes, or google-fu, will tell you that this is 
[Rockstar](https://github.com/RockstarLang/rockstar), "a dynamically typed computer programming language, designed for creating programs that are also song lyrics".

By runing the lyrics with the [online interpriter](https://codewithrockstar.com/online), you get these numbers.
```text
114
114
114
111
99
107
110
114
110
48
49
49
51
114
```
A simple ascii conversion gets the flag
```python
n = [114, 114, 114, 111, 99, 107, 110, 114, 110, 48, 49, 49, 51, 114]
print(''.join(map(chr, n)))
```
flag: `picoCTF{rrrocknrn0113r}`
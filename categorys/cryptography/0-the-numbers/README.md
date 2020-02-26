# The Numbers
We get a png.
![](./the_numbers.png)
These are obviously alphabet indices. 
```
16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }
```
```python
inp = '16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }'
flag = ''
for i in inp.split():
    if i.isdigit():
        flag += (chr((int(i))+ord('A')-1))
    else:
        flag += i

print(flag)
```
flag: `PICOCTF{THENUMBERSMASON}`
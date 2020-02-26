from pwn import *
m1 = unhex('43 467b 416e 315f 3337 6432 3466 6664 7d'.replace(' ', ''))
m2 = unhex('8573')
m3 = unhex('69 6354 3074 6861 5f'.replace(' ', ''))

# 0x1a from 2nd fread arg 
flag = bytearray("0"*0x1a, 'ascii')

flag[1] = m3[0]
flag[0] = m2[0] - 0x15
flag[2] = m3[1]
flag[4] = m1[0]
flag[5] = m3[2]

for i in range(6,10):
  flag[i] = m1[i-5] # The minus five comes from the fact that it's being pushed to the end

for i in range(10, 15):
  flag[i] = m3[i-7]

for i in range(15,26):
  flag[i] = m1[i-10]

flag[3] =  ord('o')
print(flag.decode('ascii'))
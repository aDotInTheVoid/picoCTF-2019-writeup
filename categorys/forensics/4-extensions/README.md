# extensions
We can use `file` to find out what the file realy is 
```bash
$wget https://2019shell1.picoctf.com/static/45886ed4b6d5d1dc74c4944fcf4b4041/flag.txt
--2019-10-23 01:00:43--  https://2019shell1.picoctf.com/static/45886ed4b6d5d1dc74c4944fcf4b4041/flag.txt
Resolving 2019shell1.picoctf.com (2019shell1.picoctf.com)... 3.15.247.173
Connecting to 2019shell1.picoctf.com (2019shell1.picoctf.com)|3.15.247.173|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 9984 (9.8K) [application/octet-stream]
Saving to: ‘flag.txt’

flag.txt                  100%[====================================>]   9.75K  --.-KB/s    in 0s      

2019-10-23 01:00:44 (56.0 MB/s) - ‘flag.txt’ saved [9984/9984]

$file flag.txt 
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced

$cp flag.txt flag.png
```
![](./flag.png)

flag: `picoCTF{now_you_know_about_extensions}`
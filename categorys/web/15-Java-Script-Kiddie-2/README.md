# Java Script Kiddie 2
This is similar to the previous one, but with every other key digit ignored

```js
var bytes = [];
$.get("bytes", function(resp) {
	bytes = Array.from(resp.split(" "), x => Number(x));
});
function assemble_png(u_in){
	var LEN = 16;
	var key = "00000000000000000000000000000000";
	var shifter;
	if(u_in.length == key.length){
		key = u_in;
	}
	var result = [];
	for(var i = 0; i < LEN; i++){
		shifter = Number(key.slice((i*2),(i*2)+1));
		for(var j = 0; j < (bytes.length / LEN); j ++){
			result[(j * LEN) + i] = bytes[(((j + shifter) * LEN) % bytes.length) + i]
		}
	}
	while(result[result.length-1] == 0){
		result = result.slice(0,result.length-1);
	}
	document.getElementById("Area").src = "data:image/png;base64," + btoa(String.fromCharCode.apply(null, new Uint8Array(result)));
	return false;
}
```

A similar solution works, we just need to add in the padding

```python
import itertools
KEY_LEN = 16


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
    print("key could be {}".format(key))
```
This gives
```text
key could be 80802090204020407030304000408060
key could be 80802090204020407030306000408060
key could be 80802090204020407030404000408060
key could be 80802090204020407030406000408060
key could be 80802090204020407040304000408060
key could be 80802090204020407040306000408060
key could be 80802090204020407040404000408060
key could be 80802090204020407040406000408060
key could be 80802090204060407030304000408060
key could be 80802090204060407030306000408060
key could be 80802090204060407030404000408060
key could be 80802090204060407030406000408060
key could be 80802090204060407040304000408060
key could be 80802090204060407040306000408060
key could be 80802090204060407040404000408060
key could be 80802090204060407040406000408060
```
This is not fun to try, so we instead write them all to a png, if valid.
```python
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
```
This gives a key of `80802090204020407030306000408060`, and an image 
![](./80802090204020407030306000408060.png)

Using the same decoder as last time, we get `picoCTF{f1ee7ff44419a675d1a0f0a1a91dff4c}`

---
Script adapted from [Dvd848](https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/Java_Script_Kiddie_2.md)
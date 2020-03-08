# Java Script Kiddie
```html
<html>
	<head>    
		<script src="jquery-3.3.1.min.js"></script>
		<script>
			// ******************
			// ******************
			// ** SOME JS HERE **
			// ******************
			// ******************
		</script>
	</head>
	<body>
		<center>
			<form action="#" onsubmit="assemble_png(document.getElementById('user_in').value)">
				<input type="text" id="user_in">
				<input type="submit" value="Submit">
			</form>
			<img id="Area" src=""/>
		</center>
	</body>
</html>
```
```js
var bytes = [];
$.get("bytes", function(resp) {
	bytes = Array.from(resp.split(" "), x => Number(x));
});
function assemble_png(u_in){
	var LEN = 16;
	var key = "0000000000000000";
	var shifter;
	if(u_in.length == LEN){
		key = u_in;
	}
	var result = [];
	for(var i = 0; i < LEN; i++){
		shifter = key.charCodeAt(i) - 48;
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
What this does is make a request to `/bytes`, convert the result to an array. 

Then when the user enters a key, for every number in the key (`key.charCodeAt(i) - 48` works because of how ascii is layed out) does some shifting.

Recall from our [previous adventures in png](../../forensics/7-c0rrupt/) that every png starts with an 8 byte header followed by a 13 byte IHDR chunk.

Therefor the start of any png is `89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52`. Try xxd on some png's and you'll see this.

Therefor we need to consider what shift we want to get these 16 values. 
As `i` will be from 0 to 15, the bytes we care about will only be from when `j==1`.

Then we can check if bytes at that increment gives the right bits.

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
            j = 0 # We only need to care about the first 16 bytes
            offset = (((j + shifter) * KEY_LEN) % len(bytes_arr)) + i
            if bytes_arr[offset] == expected[i]:
                shifters[i].append(shifter)               

for p in itertools.product(*shifters):
    key = "".join("{}".format(n) for n in p)
    print("key could be {}".format(key))
```
Note that as each element in the key acts separately, we need to consider every possible combination.

The output is
```text
key could be 4292148024773628
key could be 4292148024873628
key could be 4292148025773628
key could be 4292148025873628
key could be 4292748024773628
key could be 4292748024873628
key could be 4292748025773628
key could be 4292748025873628
```

This is few enough we can try them all. Luckily the first one does it.

![](./img.png)

Using an [online tool](https://zxing.org) we get the flag

Flag: `picoCTF{5184e4f12d91ca0e13de639627b4bb6a}`

---
Script adapted from [Dvd848](https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/Java_Script_Kiddie.md)
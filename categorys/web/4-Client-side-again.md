# Client-side-again
Downloading the html we get 
```html
<html>
<head>
<title>Secure Login Portal V2.0</title>
</head>
<body background="barbed_wire.jpeg" >
<!-- standard MD5 implementation -->
<script type="text/javascript" src="md5.js"></script>

<script type="text/javascript">
  var _0x5a46=['29871}','_again_d','this','Password\x20Verified','Incorrect\x20password','getElementById','value','substring','picoCTF{','not_this'];(function(_0x4bd822,_0x2bd6f7){var _0xb4bdb3=function(_0x1d68f6){while(--_0x1d68f6){_0x4bd822['push'](_0x4bd822['shift']());}};_0xb4bdb3(++_0x2bd6f7);}(_0x5a46,0x1b3));var _0x4b5b=function(_0x2d8f05,_0x4b81bb){_0x2d8f05=_0x2d8f05-0x0;var _0x4d74cb=_0x5a46[_0x2d8f05];return _0x4d74cb;};function verify(){checkpass=document[_0x4b5b('0x0')]('pass')[_0x4b5b('0x1')];split=0x4;if(checkpass[_0x4b5b('0x2')](0x0,split*0x2)==_0x4b5b('0x3')){if(checkpass[_0x4b5b('0x2')](0x7,0x9)=='{n'){if(checkpass[_0x4b5b('0x2')](split*0x2,split*0x2*0x2)==_0x4b5b('0x4')){if(checkpass[_0x4b5b('0x2')](0x3,0x6)=='oCT'){if(checkpass[_0x4b5b('0x2')](split*0x3*0x2,split*0x4*0x2)==_0x4b5b('0x5')){if(checkpass['substring'](0x6,0xb)=='F{not'){if(checkpass[_0x4b5b('0x2')](split*0x2*0x2,split*0x3*0x2)==_0x4b5b('0x6')){if(checkpass[_0x4b5b('0x2')](0xc,0x10)==_0x4b5b('0x7')){alert(_0x4b5b('0x8'));}}}}}}}}else{alert(_0x4b5b('0x9'));}}
</script>
<div style="position:relative; padding:5px;top:50px; left:38%; width:350px; height:140px; background-color:gray">
<div style="text-align:center">
<p>New and Improved Login</p>

<p>Enter valid credentials to proceed</p>
<form action="index.html" method="post">
<input type="password" id="pass" size="8" />
<br/>
<input type="submit" value="verify" onclick="verify(); return false;" />
</form>
</div>
</div>
</body>
</html>
```
The interesting js is
```js
  var _0x5a46=['29871}','_again_d','this','Password\x20Verified','Incorrect\x20password','getElementById','value','substring','picoCTF{','not_this'];(function(_0x4bd822,_0x2bd6f7){var _0xb4bdb3=function(_0x1d68f6){while(--_0x1d68f6){_0x4bd822['push'](_0x4bd822['shift']());}};_0xb4bdb3(++_0x2bd6f7);}(_0x5a46,0x1b3));var _0x4b5b=function(_0x2d8f05,_0x4b81bb){_0x2d8f05=_0x2d8f05-0x0;var _0x4d74cb=_0x5a46[_0x2d8f05];return _0x4d74cb;};function verify(){checkpass=document[_0x4b5b('0x0')]('pass')[_0x4b5b('0x1')];split=0x4;if(checkpass[_0x4b5b('0x2')](0x0,split*0x2)==_0x4b5b('0x3')){if(checkpass[_0x4b5b('0x2')](0x7,0x9)=='{n'){if(checkpass[_0x4b5b('0x2')](split*0x2,split*0x2*0x2)==_0x4b5b('0x4')){if(checkpass[_0x4b5b('0x2')](0x3,0x6)=='oCT'){if(checkpass[_0x4b5b('0x2')](split*0x3*0x2,split*0x4*0x2)==_0x4b5b('0x5')){if(checkpass['substring'](0x6,0xb)=='F{not'){if(checkpass[_0x4b5b('0x2')](split*0x2*0x2,split*0x3*0x2)==_0x4b5b('0x6')){if(checkpass[_0x4b5b('0x2')](0xc,0x10)==_0x4b5b('0x7')){alert(_0x4b5b('0x8'));}}}}}}}}else{alert(_0x4b5b('0x9'));}}
```
[formating](https://www.freeformatter.com/javascript-beautifier.html) gives
```js
var _0x5a46 = ['29871}', '_again_d', 'this', 'Password\x20Verified', 'Incorrect\x20password', 'getElementById', 'value', 'substring', 'picoCTF{', 'not_this'];
(function (_0x4bd822, _0x2bd6f7) {
	var _0xb4bdb3 = function (_0x1d68f6) {
		while (--_0x1d68f6) {
			_0x4bd822['push'](_0x4bd822['shift']());
		}
	};
	_0xb4bdb3(++_0x2bd6f7);
}(_0x5a46, 0x1b3));
var _0x4b5b = function (_0x2d8f05, _0x4b81bb) {
	_0x2d8f05 = _0x2d8f05 - 0x0;
	var _0x4d74cb = _0x5a46[_0x2d8f05];
	return _0x4d74cb;
};

function verify() {
	checkpass = document[_0x4b5b('0x0')]('pass')[_0x4b5b('0x1')];
	split = 0x4;
	if (checkpass[_0x4b5b('0x2')](0x0, split * 0x2) == _0x4b5b('0x3')) {
		if (checkpass[_0x4b5b('0x2')](0x7, 0x9) == '{n') {
			if (checkpass[_0x4b5b('0x2')](split * 0x2, split * 0x2 * 0x2) == _0x4b5b('0x4')) {
				if (checkpass[_0x4b5b('0x2')](0x3, 0x6) == 'oCT') {
					if (checkpass[_0x4b5b('0x2')](split * 0x3 * 0x2, split * 0x4 * 0x2) == _0x4b5b('0x5')) {
						if (checkpass['substring'](0x6, 0xb) == 'F{not') {
							if (checkpass[_0x4b5b('0x2')](split * 0x2 * 0x2, split * 0x3 * 0x2) == _0x4b5b('0x6')) {
								if (checkpass[_0x4b5b('0x2')](0xc, 0x10) == _0x4b5b('0x7')) {
									alert(_0x4b5b('0x8'));
								}
							}
						}
					}
				}
			}
		}
	} else {
		alert(_0x4b5b('0x9'));
	}
}
```
Even this is quite unreadeble, but with some renaming we get

```js
var parts = ['29871}', '_again_d', 'this', 'Password\x20Verified', 'Incorrect\x20password', 'getElementById', 'value', 'substring', 'picoCTF{', 'not_this'];
(
    function (list, number) {
	var helper = function (number2) {
		while (--number2) {
			list['push'](list['shift']());
		}
	};
	helper(++number);
}(parts, 0x1b3));

var part = function (index, nothing) {
	index = index - 0x0;
	var ret = parts[index];
	return ret;
};

function verify() {
	checkpass = document[part('0x0')]('pass')[part('0x1')];
	split = 0x4;
	if (checkpass[part('0x2')](0x0, split * 0x2) == part('0x3')) {
		if (checkpass[part('0x2')](0x7, 0x9) == '{n') {
			if (checkpass[part('0x2')](split * 0x2, split * 0x2 * 0x2) == part('0x4')) {
				if (checkpass[part('0x2')](0x3, 0x6) == 'oCT') {
					if (checkpass[part('0x2')](split * 0x3 * 0x2, split * 0x4 * 0x2) == part('0x5')) {
						if (checkpass['substring'](0x6, 0xb) == 'F{not') {
							if (checkpass[part('0x2')](split * 0x2 * 0x2, split * 0x3 * 0x2) == part('0x6')) {
								if (checkpass[part('0x2')](0xc, 0x10) == part('0x7')) {
									alert(part('0x8'));
								}
							}
						}
					}
				}
			}
		}
	} else {
		alert(part('0x9'));
	}
}
```
This starts by declaring a array of strings that will be needed later.

Then it runs a function to rearrange the strings

Then it declares a function to index into the list.

Note that this functions ~~ab~~uses js's *interesting* ideas about a function call.

```js
Welcome to Node.js v13.10.1.
Type ".help" for more information.
> a = [1,2,3]
[ 1, 2, 3 ]
> a["push"](4)
4
> a
[ 1, 2, 3, 4 ]
```

Anyway the first thing we can do is run the function to get the array as it is used

```js
Welcome to Node.js v13.10.1.
Type ".help" for more information.
> var parts = ['29871}', '_again_d', 'this', 'Password\x20Verified', 'Incorrect\x20password', 'getElementById', 'value', 'substring', 'picoCTF{', 'not_this'];
undefined
> (
...     function (list, number) {
.....   var helper = function (number2) {
.......                 while (--number2) {
.........                       list['push'](list['shift']());
.........               }
.......         };
.....   helper(++number);
..... }(parts, 0x1b3));
undefined
> parts
[
  'getElementById',
  'value',
  'substring',
  'picoCTF{',
  'not_this',
  '29871}',
  '_again_d',
  'this',
  'Password Verified',
  'Incorrect password'
]
```

From here you could make a pretty good guess at the password. But that's no fun.

The `part` functions is their to cast to int. By evaluating that and other expressions in `node` we get:

```js
function verify() {
    checkpass = document.getElementById('pass').value;
    if (checkpass.substring(0, 8) == 'picoCTF') {
        if (checkpass.substring(7, 9) == '{n') {
            if (checkpass.substring(8, 16) == 'not_this') {
                if (checkpass.substring(3, 6) == 'oCT') {
                    if (checkpass.substring(24, 32) == '29871}') {
                        if (checkpass.substring(6, 11) == 'F{not') {
                            if (checkpass.substring(16, 24) == '_again_d') {
                                if (checkpass.substring(12, 16) == 'this') {
                                    alert('Password Verified');
                                }
                            }
                        }
                    }
                }
            }
        }
    } else {
        alert('Incorrect password');
    }
}
```
From here it's easy to see the password is `picoCTF{not_this_again_d29871}`
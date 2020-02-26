# Binary Exploitation

We will use the excelent [`pwntools`](https://docs.pwntools.com/en/stable/).

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install pwntools
```

Then create a .env file to store your login. Eg:

```text
PICOUSER=your_name_here
PICOPSWD=your_password_here
```
Then you can use python to check
```text
$ source .env
$ python3
Python 3.7.6 (default, Dec 30 2019, 19:38:28)
[Clang 11.0.0 (clang-1100.0.33.16)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from os import environ
>>> environ["PICOUSER"]
'yeswriteup'
>>>
```
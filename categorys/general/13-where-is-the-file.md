# where-is-the-file
In unix, files starting with with `.` are hidden. To see them use the `-a` flag.

On their server:
```bash
$ cd /problems/where-is-the-file_5_5302300652950d2248ac8bb0042d115e
$ ls -a
.  ..  .cant_see_me
$ cat .cant_see_me 
picoCTF{w3ll_that_d1dnt_w0RK_a871629e}
```
flag: `picoCTF{w3ll_that_d1dnt_w0RK_a871629e}`

# picobrowser

The site want's your [User Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) to be `picobrowser`

For stuff like this it's easier to use the command line, as firefox doesn't want to let you pretend to be another browser, as it's bad fro ratings.

[`curl --user-agent picobrowser https://2019shell1.picoctf.com/problem/32205/flag | grep picoCTF`](https://explainshell.com/explain?cmd=curl+--user-agent+picobrowser+https%3A%2F%2F2019shell1.picoctf.com%2Fproblem%2F32205%2Fflag+%7C+grep+picoCTF)

Flag: `picoCTF{p1c0_s3cr3t_ag3nt_ee951878}`
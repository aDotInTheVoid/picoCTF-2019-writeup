# where are the robots
[`robots.txt`](https://support.google.com/webmasters/answer/6062608?hl=en) 
are uses to tell web scrapers which pages they can and cant access.

Going to [`https://2019shell1.picoctf.com/problem/12267/robots.txt`](https://2019shell1.picoctf.com/problem/12267/robots.txt) gives
```text
User-agent: *
Disallow: /713d3.html
```

From here it's clear we should visit [`713d3.html`](https://2019shell1.picoctf.com/problem/12267/713d3.html), which has the flag

Flag: `picoCTF{ca1cu1at1ng_Mach1n3s_713d3}`

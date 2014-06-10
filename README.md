chalk
=====

####*A Light-weight python package for terminal output in color*

*"Color printing so easy, makes you wanna smack yo' momma."*

**Overview**

Chalk allows you to print to your terminal in color. It also provides a simple
`logging` handler and formatter for a more informative logging experience.
Why print in black and white?

**Installation:**

    pip install pychalk


**In Module Usage:**

[`examples/example-module.py`](examples/example-module.py)

![example-module.py](images/module.png)


**Logging:**

[`examples/example-log.py`](examples/example-log.py)

![example-log.py](images/log.png)


**Testing:**


```
$ git clone https://github.com/anthonyalmarza/chalk.git
$ cd chalk
$ vitrualenv venv --no-site-packages --distribute
$ source venv/bin/activate
$ pip install nose
$ nosetests -w chalk tests # or simply python -m unittest chalk.tests
......
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```


**Big-ups**

* @billjohnston
* @livibetter

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

```python
import chalk

chalk.blue("Hello world!!")
chalk.yellow("Listen to me!!!")
chalk.red("ERROR", pipe=chalk.stderr)
chalk.magenta('This is pretty cool', opts='bold')
chalk.cyan('...more stuff', opts=('bold', 'underscore'))
```


**Logging:**

```python
import logging
from chalk import log

logger = logging.getLogger(__name__)

handler = log.ChalkHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.error('Error!!!!')
```

**Testing:**

After cloning the repo...

    anthony@lappy6000:~/git/$ cd chalk

    anthony@lappy6000:~/git/chalk$ vitrualenv venv --no-site-packages --distribute

    anthony@lappy6000:~/git/chalk$ source venv/bin/activate

    (venv)anthony@lappy6000:~/git/chalk$ pip install nose

    (venv)anthony@lappy6000:~/git/chalk$ nosetests chalk.tests
    ......
    ----------------------------------------------------------------------
    Ran 6 tests in 0.002s

    OK


**Big-ups**

@billjohnston..

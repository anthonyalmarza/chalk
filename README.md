chalk
=====

***A Light-weight python package for terminal output in color***

*"Color printing so easy, makes you wanna smack yo' momma."*

Installation:

    pip install pychalk


In Module Usage:

```python
import chalk

chalk.blue("Hello world!!")
chalk.yellow("Listen to me!!!")
chalk.red("ERROR", pipe=chalk.stderr)
chalk.magenta('This is pretty cool', opts='bold')
chalk.cyan('...more stuff', opts=('bold', 'underscore'))
```


Logging:

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

Bigups go to @billjohnston - you know why fella.

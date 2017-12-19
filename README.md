# Chalk

[![CircleCI](https://circleci.com/gh/anthonyalmarza/chalk.svg?style=svg)](https://circleci.com/gh/anthonyalmarza/chalk)

[![codecov](https://codecov.io/gh/anthonyalmarza/chalk/branch/master/graph/badge.svg)](https://codecov.io/gh/anthonyalmarza/chalk)

*A Light-weight python package for terminal output in color*

## Overview

Chalk allows you to print to your terminal in color. It also provides a simple
`logging` handler and formatter for a more informative logging experience.
Why print in black and white?

### Installation

  pip install pychalk

### Usage

```python
from __future__ import print_function
import chalk

print(chalk.red('foo'))
```

```python
import chalk

white = chalk.Chalk('white')
white('foo', bold=True, underline=True)
# returns '\x1b[37;1;4mfoo\x1b[0m'

bold_white = white + chalk.utils.FontFormat('bold')
bold_white('foo')
# returns '\x1b[37;1mfoo\x1b[0m'

bold_white + 'foo'
# returns '\x1b[37;1mfoo'

bold_white + 'foo' + chalk.RESET
# returns '\x1b[37;1mfoo/x1b[0m'
```

### Testing

Install `pyenv`

```bash
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
pyenv install -s -v 2.7.14 \
&& pyenv install -s -v 3.5.4 \
&& pyenv install -s -v 3.6.3
```

Then install the development requirements... To help with this please use:

```bash
./bin/install
```

Then run the tests using tox.

```bash
source venv/bin/activate
tox
py27 develop-inst-noop: /home/anthony/git/chalk

...

Ran 37 tests in 0.009s

OK
py36 runtests: commands[1] | coverage report -m
Name                Stmts   Miss  Cover   Missing
-------------------------------------------------
chalk/__init__.py      18      0   100%
chalk/logging.py       28      0   100%
chalk/utils.py        124      0   100%
-------------------------------------------------
TOTAL                 170      0   100%
_________________________________________________________________________________________ summary _________________________________________________________________________________________
  py27: commands succeeded
  py35: commands succeeded
  py36: commands succeeded
  congratulations :)
```

#### Using Docker

Alternatively use a docker image with pyenv installed. This project uses
`anthonyalmarza/alpine-pyenv:cable` which has pyenv setup with the latest
versions of python 2.7, 3.5 and 3.6 (as of Dec 19th 2017).

First build the image and tag it as `chalk`

```bash
./bin/local/build
```

Then run the tests

```bash
./bin/local/test
```

### Thank you

* @billjohnston
* @livibetter

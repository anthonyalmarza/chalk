"""
Chalk is a very light-weight module for printing to the terminal in color.
Usage:
    import chalk

    chalk.blue("Hello world!!")
    chalk.yellow("Listen to me!!!")
    chalk.red("ERROR")
    chalk.magenta('This is pretty cool', bold=True)
    chalk.cyan('...more stuff', bold=True, underline=True)
"""
from __future__ import absolute_import, print_function, unicode_literals
from six import string_types
from . import logging, utils
from .utils import Chalk, FontFormat, RESET, eraser

__all__ = (
    'logging',
    'utils',
    'Chalk',
    'RESET',
    'eraser',
    'bold',
    'underline',
    'blink',
    'reverse',
    'hide',
    'black',
    'red',
    'blue',
    'green',
    'yellow',
    'magenta',
    'cyan',
    'white'
)

# pylint: disable=C0103
bold = FontFormat('bold')
underline = FontFormat('underline')
blink = FontFormat('blink')
reverse = FontFormat('reverse')
hide = FontFormat('hide')

black = Chalk('black')
red = Chalk('red')
blue = Chalk('blue')
green = Chalk('green')
yellow = Chalk('yellow')
magenta = Chalk('magenta')
cyan = Chalk('cyan')
white = Chalk('white')

"""
Chalk is a very light-weight module for printing to the terminal in color.
Usage:
    import chalk

    chalk.blue("Hello world!!")
    chalk.yellow("Listen to me!!!")
    chalk.red("ERROR", pipe=chalk.stderr)
    chalk.magenta('This is pretty cool', opts='bold')
    chalk.cyan('...more stuff', opts=('bold', 'underscore'))
"""
from collections import namedtuple
from os import linesep
from sys import stdout, modules, version_info


__version__ = "1.0.0"

PY3 = (version_info >= (3, 0))

COLORS = (
    'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
)

FORMATS = ('reset', 'bold', 'underscore', 'blink', 'reverse', 'hide')

Format = namedtuple('Format', FORMATS)
Color = namedtuple('Color', COLORS)

_esc = "\x1b[%sm"
_clear_formatting = _esc % "0"

# ansi standards http://ascii-table.com/ansi-escape-sequences.php
fnt = Format('0', '1', '4', '5', '7', '8')
fgs = Color(*['3%d' % i for i in range(8)])
bgs = Color(*['4%d' % i for i in range(8)])


def make_code(fg, bg=None, opts=None):
    "makes the visualization escape code"
    value = '%s'
    if opts and isinstance(opts, str):
        opts = (opts,)
    elif opts and not any(isinstance(opts, typo) for typo in (list, tuple)):
        raise TypeError("opts expects a strict iterable. e.g. (x,)")
    parts = [value % getattr(fnt, attr) for attr in opts] if opts else []
    parts.append(value % getattr(fgs, fg))
    if bg:
        parts.append(value % getattr(bgs, bg))
    return _esc % ';'.join(parts)

def convert_to_str(obj):
    "Attempts to convert given object to a string object"
    if not isinstance(obj, str):
        if PY3 and (type(obj) == bytes):
            obj = obj.decode("utf-8")
        else:
            obj = str(obj)
    return obj


def format_txt(fg, txt, bg, opts):
    txt = convert_to_str(txt)
    fg = convert_to_str(fg)

    if bg != None:
        bg = convert_to_str(bg)
    if opts != None:
        opts = convert_to_str(opts)

    return make_code(fg, bg, opts) + txt + _clear_formatting


def format_factory(fg):
    def _format_txt(txt, bg=None, opts=None):
        return format_txt(fg, txt, bg, opts)
    return _format_txt


def chalk(fg):
    "A factory function that return piece of chalk"
    def _chalk(txt, bg=None, pipe=stdout, opts=None):
        "A piece of chalk that you call by color"
        pipe.write(format_txt(fg, txt, bg, opts))
        pipe.write(linesep)
    return _chalk

__module__ = modules[__name__]

# The chalk factory: makes chalk.red, chalk.blue, ... etcetera available.
for color in COLORS:
    setattr(__module__, color, chalk(color))
    setattr(__module__, 'format_%s' % color, format_factory(color))


def eraser():
    "Equivalent to running bash 'clear' command"
    stdout.write('\x1b[2J\x1b[0;0H' + linesep)
    return

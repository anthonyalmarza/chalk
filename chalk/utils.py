from __future__ import absolute_import, print_function
from os import linesep
from sys import version_info
from six import python_2_unicode_compatible, string_types
from six.moves import map


# ansi standards http://ascii-table.com/ansi-escape-sequences.php
COLOR_NAMES = (
    'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
)
COLOR_SET = set(COLOR_NAMES)
COLOR_MAP = dict(zip(COLOR_NAMES, map(str, range(len(COLOR_NAMES)))))


FORMAT_NAMES = ('bold', 'underline', 'blink', 'reverse', 'hide')
FORMAT_VALUES = ('1', '4', '5', '7', '8')
FORMAT_SET = set(FORMAT_NAMES)
FORMAT_MAP = dict(zip(FORMAT_NAMES, FORMAT_VALUES))
ESC = '\x1b[%sm'
RESET = ESC % '0'


@python_2_unicode_compatible
class Style(object):
    """Style is a callable, mutable unicode styling base class.
        Usage:
            style = Style(1)
            bold_text = style('foo')  # '\x1b[1mfoo\x1b[0m'
            style += Style(32)
            green_bold_text = style('bar')  # '\x1b[1;32mfoo\x1b[0m'

            print(style + 'baz')  # prints baz as green bold text
    """

    __slots__ = ['value']

    def __init__(self, value):
        self.value = to_str(value)

    def __add__(self, other):
        if isinstance(other, string_types):
            return str(self) + other
        elif not isinstance(other, Style):
            raise TypeError(
                'concat operator is only supported for string and Style types'
            )
        return other.__radd__(self)

    def __radd__(self, other):
        if isinstance(other, string_types):
            return other + str(self)
        return Style(';'.join([other.value, self.value]))

    def __iadd__(self, other):
        self.value = self.__add__(other).value
        return self

    def __str__(self):
        return ESC % self.value

    def __eq__(self, other):
        return other == str(self)

    def __ne__(self, other):
        return other != str(self)

    def __call__(self, txt, reset=True, new_line=False):
        txt = to_str(txt)
        if reset:
            txt += RESET
        if new_line:
            txt += linesep
        return str(self) + txt

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.value)

    def clone(self):
        """Replicates the current instance, without being effected by the
            modified behaviour of any subclasses.
        """
        return Style(self.value)


class FontFormat(Style):
    """chalk.utils.Style subclass
        Usage:
            style = FontFormat('bold')
            bold_text = style('foo')  # '\x1b[1mfoo\x1b[0m'
            style += FontFormat('underline')
            bold_underlined_text = style('bar')  # '\x1b[1;4mbar\x1b[0m'
    """

    def __init__(self, value):
        super(FontFormat, self).__init__(value)
        if self.value in FORMAT_SET:
            self.value = FORMAT_MAP[self.value]
        elif self.value not in FORMAT_VALUES:
            raise ValueError(
                'FontFormat values should be a member of: {}'.format(
                    ', '.join(FORMAT_NAMES + FORMAT_VALUES)
                )
            )


class Color(Style):
    """chalk.utils.Style subclass: Base class to facilitate referencing colors
        by name.
        Usage:
            class ForegroundColor(Color):
                PREFIX = 3

            style = ForegroundColor('red')
            red_txt = style('foo')  # '\x1b[31mfoo\x1b[0m'
    """

    PREFIX = NotImplemented

    def __init__(self, value):
        super(Color, self).__init__(value)
        self.value = self.get_color(self.value)

    def get_color(self, value):
        """Helper method to validate and map values used in the instantiation of
            of the Color object to the correct unicode value.
        """
        if value in COLOR_SET:
            value = COLOR_MAP[value]
        else:
            try:
                value = int(value)
                if value >= 8:
                    raise ValueError()
            except ValueError as exc:
                raise ValueError(
                    'Colors should either a member of: {} or a positive '
                    'integer below 8'.format(', '.join(COLOR_NAMES))
                )
        return '{}{}'.format(self.PREFIX, value)


class ForegroundColor(Color):
    """chalk.utils.Color subclass
        Usage:
            style = ForegroundColor('red')
            red_txt = style('foo')  # '\x1b[31mfoo\x1b[0m'
    """
    PREFIX = 3


class BackgroundColor(Color):
    """chalk.utils.Color subclass
        Usage:
            style = BackgroundColor('red')
            red_txt = style('foo')  # '\x1b[41mfoo\x1b[0m'
    """
    PREFIX = 4


@python_2_unicode_compatible
class Chalk(object):
    """Instances of the Chalk class serve to leverage the properties of
        chalk.utils.Style by exposing itself as a callable interface.
        Usage:
            white = Chalk('white')
            white('foo', bold=True, underline=True)
            # returns '\x1b[37;1;4mfoo\x1b[0m'

            bold_white = white + FontFormat('bold')
            bold_white('foo')
            # returns '\x1b[37m\x1b[1mfoo\x1b[0m'

            bold_white + 'foo'
            # returns '\x1b[37;1;4mfoo'
    """

    __slots__ = ['style']

    def __init__(self, foreground_or_style, background=None):
        if isinstance(foreground_or_style, Style):
            self.style = foreground_or_style
        else:
            self.style = ForegroundColor(foreground_or_style)
        if background is not None:
            self.style += BackgroundColor(background)

    def __add__(self, other):
        if isinstance(other, string_types):
            return str(self) + other
        elif isinstance(other, (Chalk, Style)):
            chalk = self.clone()
            chalk += other
            return chalk
        raise ValueError(
            'concat operator is only supported for string and Style types'
        )

    def __radd__(self, other):
        return other.__add__(str(self))

    def __iadd__(self, other):
        if not isinstance(other, (Style, Chalk)):
            raise ValueError(
                'concat operator is only supported for string and Style types'
            )
        self.style += other
        return self

    def __call__(self, txt, reset=True, new_line=False, **kwargs):
        style = self.get_style(**kwargs)
        return style(txt, reset=reset, new_line=new_line)

    def get_style(self, **kwargs):
        """Helper method to ensure that the instantiated style isn't impacted
            by each execution of __call__
        """
        style = self.style.clone()
        for key, value in kwargs.items():
            if value and key in FORMAT_SET:
                style += FontFormat(FORMAT_MAP[key])
            elif key == 'foreground':
                style += ForegroundColor(value)
            elif key == 'background':
                style += BackgroundColor(value)
        return style

    def __eq__(self, other):
        return other == self.style

    def __ne__(self, other):
        return other != self.style

    def __str__(self):
        return str(self.style)

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self)

    def clone(self):
        return self.__class__(self.style.clone())


def eraser(new_line=False):
    """Equivalent to running bash 'clear' command
    """
    output = '\x1b[2J\x1b[0;0H'
    if new_line:
        output += linesep
    return output


PY3 = (version_info >= (3, 0))


def to_str(obj):
    """Attempts to convert given object to a string object
    """
    if not isinstance(obj, str) and PY3 and isinstance(obj, bytes):
        obj = obj.decode('utf-8')
    return obj if isinstance(obj, string_types) else str(obj)

from __future__ import absolute_import, print_function

import unittest

import six

import chalk
from chalk.utils import (
    BackgroundColor,
    Chalk,
    Color,
    FontFormat,
    ForegroundColor,
    Style
)


COLORS = (
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white'
)


class TestChalkUtils(unittest.TestCase):

    def test_style_add_string(self):
        bold = Style(1)
        actual = bold + 'foo'
        expected = '\x1b[1mfoo'
        self.assertEqual(actual, expected)

    def test_style_radd_string(self):
        bold = Style(1)
        actual = 'foo' + bold
        expected = 'foo\x1b[1m'
        self.assertEqual(actual, expected)

    def test_style_add_type_error(self):
        bold = Style(1)

        def concat(item1, item2):
            return item1 + item2

        self.assertRaises(TypeError, concat, bold, 1)

    def test_style_repr(self):
        bold = Style(1)
        self.assertEqual(repr(bold), '<Style: 1>')

    def test_style_new_line_option(self):
        bold = Style(1)
        actual = bold('foo', new_line=True)
        expected = '\x1b[1mfoo\x1b[0m\n'
        self.assertEqual(actual, expected)

    def test_font_format_inheritance(self):
        self.assertTrue(issubclass(FontFormat, Style))

    def test_font_format_init_error(self):
        self.assertRaises(ValueError, FontFormat, 100)

    def test_background_color_inheritance(self):
        self.assertTrue(issubclass(BackgroundColor, Color))

    def test_foreground_color_inheritance(self):
        self.assertTrue(issubclass(ForegroundColor, Color))

    def test_color_init_errors(self):
        self.assertRaises(ValueError, Color, 10)
        self.assertRaises(ValueError, Color, 'ruby')

    def test_chalk_init(self):
        white = Chalk('white', 'black')
        self.assertIsInstance(white, Chalk)
        self.assertIsInstance(white.style, Style)
        self.assertEqual(str(white.style), '\x1b[37;40m')

    def test_chalk_add(self):
        red = Chalk('red')
        actual = red + 'foo'
        expected = '\x1b[31mfoo'
        self.assertEqual(actual, expected)

    def test_chalk_radd(self):
        red = Chalk('red')
        actual = 'foo' + red
        expected = 'foo\x1b[31m'
        self.assertEqual(actual, expected)

    def test_chalk_add_error(self):
        red = Chalk('red')
        self.assertRaises(ValueError, lambda x: x + 1, red)

    def test_chalk_iadd(self):
        red = Chalk('red')
        red += FontFormat('bold')
        self.assertEqual(red, '\x1b[31;1m')

    def test_chalk_iadd_error(self):
        red = Chalk('red')
        def update(item):
            item += 1
        self.assertRaises(ValueError, update, red)

    def test_chalk_get_style_foreground(self):
        red = Chalk('red')
        style = red.get_style(foreground='white')
        self.assertEqual(style, '\x1b[31;37m')

    def test_chalk_get_style_bold(self):
        red = Chalk('red')
        style = red.get_style(bold=True)
        self.assertEqual(style, '\x1b[31;1m')

    def test_chalk_repr(self):
        red = Chalk('red')
        self.assertEqual(repr(red), '<Chalk: \x1b[31m>')

    def test_chalk_ne(self):
        self.assertNotEqual(Chalk('white'), Chalk('blue'))

    def test_style_ne(self):
        self.assertNotEqual(Style(1), '\x1b[4m')

    def test_chalk_eraser(self):
        self.assertEqual(chalk.eraser(), '\x1b[2J\x1b[0;0H')

    def test_chalk_eraser_new_line(self):
        self.assertEqual(chalk.eraser(new_line=True), '\x1b[2J\x1b[0;0H\n')

    def test_chalk_concat_style(self):
        new_chalk = chalk.white + Style(1)
        self.assertIsInstance(new_chalk, Chalk)
        self.assertIsNot(new_chalk, chalk.white)
        self.assertEqual(new_chalk, '\x1b[37;1m')

    def test_formats(self):
        "ensure completeness and correctness of formats"
        format_name_value_pairs = {
            'bold': '1',
            'underline': '4',
            'blink': '5',
            'reverse': '7',
            'hide': '8',
        }
        for key, value in list(format_name_value_pairs.items()):
            self.assertEqual(chalk.utils.FORMAT_MAP[key], value)

    def test_colors(self):
        "ensure the list and spelling of colors is correct"
        self.assertEqual(chalk.utils.COLOR_NAMES, COLORS)

    def test_foreground_and_background_color_basic_use(self):
        "ensure basic functionality"
        actual = ForegroundColor('red') + BackgroundColor('blue')
        expected = '\x1b[31;44m'
        self.assertEqual(str(actual), expected)

    def test_make_code_with_opts(self):
        "ensure use of optional formats"
        actual = ForegroundColor('green') + BackgroundColor('magenta') + chalk.bold
        expected = '\x1b[32;45;1m'
        self.assertEqual(str(actual), expected)

        actual = ForegroundColor('black') + BackgroundColor('white') + chalk.bold + chalk.underline
        expected = '\x1b[30;47;1;4m'
        self.assertEqual(str(actual), expected)

    def test_chalk_class_accepts_bytes(self):
        actual = Chalk(b'white')(b'hello', background=b'black')
        expected = '\x1b[37;40mhello\x1b[0m'
        self.assertEqual(actual, expected)

    def test_format_txt_accepts_unicode(self):
        actual = chalk.white('abcd' + six.unichr(5000), background='black')
        expected = six.u('\x1b[37;40mabcd\u1388\x1b[0m')
        self.assertEqual(actual, expected)

    def test_existance_of_needed_functions(self):
        "ref test name"
        for color in COLORS:
            self.assertTrue(
                hasattr(chalk, color),
                'chalk does not have the color: {}'.format(color)
            )

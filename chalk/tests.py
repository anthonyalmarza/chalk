import unittest

import chalk


COLORS = (
    'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
)


class TestChalk(unittest.TestCase):

    def test_formats(self):
        "ensure completeness and correctness of formats"
        format_name_value_pairs = {
            'reset': '0',
            'bold': '1',
            'underscore': '4',
            'blink': '5',
            'reverse': '7',
            'hide': '8',
        }
        for key, value in list(format_name_value_pairs.items()):
            self.assertEqual(getattr(chalk.fnt, key), value)

    def test_colors(self):
        "ensure the list and spelling of colors is correct"
        self.assertEqual(chalk.COLORS, COLORS)

    def test_make_code_basic_use(self):
        "ensure basic functionality"
        actual = chalk.make_code('red', 'blue')
        expected = '\x1b[31;44m'
        self.assertEqual(actual, expected)

    def test_make_code_with_opts(self):
        "ensure use of optional formats"
        actual = chalk.make_code('green', 'magenta', opts='bold')
        expected = '\x1b[1;32;45m'
        self.assertEqual(actual, expected)

        actual = chalk.make_code('black', 'white', opts=('bold', 'underscore'))
        expected = '\x1b[1;4;30;47m'
        self.assertEqual(actual, expected)

        self.assertRaises(
            TypeError, chalk.make_code, ('black', 'white'), {'opts': ('bold')}
        )

    def test_format_txt(self):
        "sometimes doc strings are useless"
        actual = chalk.format_txt('white', 'hello', 'black', None)
        expected = "\x1b[37;40mhello\x1b[0m"
        self.assertEqual(actual, expected)

    def test_existance_of_needed_functions(self):
        "ref test name"
        for color in COLORS:
            getattr(chalk, color)

        for color in COLORS:
            getattr(chalk, 'format_' + color)

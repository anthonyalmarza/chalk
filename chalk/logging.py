from __future__ import absolute_import, print_function
import logging

import chalk


def get_chalk(level):
    """Gets the appropriate piece of chalk for the logging level
    """
    if level >= logging.ERROR:
        _chalk = chalk.red
    elif level >= logging.WARNING:
        _chalk = chalk.yellow
    elif level >= logging.INFO:
        _chalk = chalk.blue
    elif level >= logging.DEBUG:
        _chalk = chalk.green
    else:
        _chalk = chalk.white
    return _chalk


class ChalkFormatter(logging.Formatter):
    """logging.Formatter subclass that colors the emitted record based on its
        level.
            logging.ERROR+ => red
            logging.WARNING+ => yello
            logging.INFO+ => blue
            logging.DEBUG+ => green
            lower than logging.DEBUG => white
    """

    def format(self, record):
        output = super(ChalkFormatter, self).format(record)
        level = record.levelno
        _chalk = get_chalk(level)
        return _chalk(output)

    def formatException(self, ei):
        exception = super(ChalkFormatter, self).formatException(ei)
        return chalk.red(exception)


class ChalkHandler(logging.StreamHandler):
    """logging.StreamHandler subclass that by default implements an instance
        of ChalkFormatter as its default formatter.
    """

    def __init__(self, stream=None):
        super(ChalkHandler, self).__init__(stream=stream)
        # add the default formatter
        self.formatter = ChalkFormatter()


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # Configure the logging formatters
    'formatters': {
        'verbose': {
            '()': 'chalk.log.ChalkFormatter',
            'format': (
                '-------------------\n'
                'pid %(process)d - %(name)s %(levelname)s %(asctime)s '
                '%(module)s.%(funcName)s line: %(lineno)d : %(message)s\n'
                '-------------------'
            ),
            'datefmt': '%H:%M:%S'
        }
    },

    # Configure the handlers, specifying the formatter is optional.
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },

    # Configure your loggers.
    'loggers': {
        '': {
            'handlers': ['console', ],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}

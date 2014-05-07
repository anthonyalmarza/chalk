import chalk
import logging
import sys

def getChalkColor(level):
    "gets the appropriate piece of chalk for the logging level"
    if level >= logging.ERROR:
        _chalk = chalk.format_red
    elif level >= logging.WARNING:
        _chalk = chalk.format_yellow
    elif level >= logging.INFO:
        _chalk = chalk.format_blue
    elif level >= logging.DEBUG:
        _chalk = chalk.format_green
    return _chalk


class ChalkFormatter(logging.Formatter):

    def formatMessage(self, record):
        message = super(ChalkFormatter, self).formatMessage(record)
        level = record.levelno
        _chalk = getChalkColor(level)
        return _chalk(message)

    def format(self, record):
        if sys.version_info[0] < 3:
            level = record.levelno
            _chalk = getChalkColor(level)
            self._fmt = _chalk(self._fmt)
        return super(ChalkFormatter, self).format(record)

    def formatException(self, ei):
        exception = super(ChalkFormatter, self).formatException(ei)
        return chalk.format_red(exception)


class ChalkHandler(logging.StreamHandler):

    def format(self, record):
        """
        Format the specified record.

        If a formatter is set, use it. Otherwise, use the default formatter
        for the module.
        """
        if self.formatter:
            fmt = self.formatter
        else:
            fmt = ChalkFormatter()
        return fmt.format(record)

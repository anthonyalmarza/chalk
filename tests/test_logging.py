from __future__ import absolute_import, print_function

import logging
import unittest

from chalk.logging import ChalkFormatter, ChalkHandler
from six import python_2_unicode_compatible


@python_2_unicode_compatible
class FakeStream(object):
    """Utility class used to mimic a stream and hold each emitted record in
        memory
    """

    def __init__(self):
        self.msgs = []

    def write(self, msg):
        self.msgs.append(msg)

    def __str__(self):
        return ''.join(self.msgs)

    def __contains__(self, item):
        return item in str(self)

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.msgs)


logger = logging.getLogger(__name__)
logger.setLevel(1)


class TestChalkLogging(unittest.TestCase):

    def setUp(self):
        super(TestChalkLogging, self).setUp()
        self.stream = FakeStream()
        self.handler = ChalkHandler(stream=self.stream)
        logger.addHandler(self.handler)

    def test_handler_formatter(self):
        self.assertIsInstance(self.handler.formatter, ChalkFormatter)

    def test_exception_logging(self):
        logger.exception('exception', exc_info=Exception('Error!!!'))
        self.assertIn('\x1b[31mexception', self.stream)
        self.assertIn('\x1b[0m', self.stream)

    def test_error_logging(self):
        logger.error('error')
        self.assertIn('\x1b[31merror\x1b[0m', self.stream)

    def test_warning_logging(self):
        logger.warning('warning')
        self.assertIn('\x1b[33mwarning\x1b[0m', self.stream)

    def test_info_logging(self):
        logger.info('info')
        self.assertIn('\x1b[34minfo\x1b[0m', self.stream)

    def test_debug_logging(self):
        logger.debug('debug')
        self.assertIn('\x1b[32mdebug\x1b[0m', self.stream)

    def test_sub_debug_logging(self):
        logger.log(1, 'msg')
        self.assertIn('\x1b[37mmsg\x1b[0m', self.stream)

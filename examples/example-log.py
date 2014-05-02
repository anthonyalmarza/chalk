#!/usr/bin/env python

import logging
from chalk import log

logger = logging.getLogger(__name__)

handler = log.ChalkHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.error('Error!!!!')
logger.warning('Warning!!!!')
logger.info('Info!!!!')
logger.debug('Debug!!!!')

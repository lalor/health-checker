# -*- coding: utf8 -*-
__author__ = 'hzlaimingxing'

import logging
import traceback

from health_checker.client.handler import SyncMsgHandler
from health_checker.client.response import sync_error, sync_ok


LOG = logging.getLogger(__name__)


class Client(object):
    """wrapper for client"""

    def __init__(self):
        self.msg_handler = SyncMsgHandler()

    def __call__(self, **kwargs):
        action = kwargs.get('action', 'invalid')
        params = kwargs.get('params', {})

        try:
            result = self.msg_handler.execute(action, params)
            LOG.info("do action {0} successful".format(action))
            return sync_ok(action, result)

        except Exception as e:
            LOG.error("catch exception when handle action: {0}, err_msg: {1}".format(action, e))
            LOG.error(traceback.format_exc())
            return sync_error(action, e)
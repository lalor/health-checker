# -*- coding:UTF-8 -*-
__author__ = 'hzlaimingxing'

import logging

from health_checker.client.env import Env
from health_checker.client.util import get_disk_capacity


LOG = logging.getLogger(__name__)


class CheckBinaryLogs(object):

    def __init__(self, params):
        self.params= params

    def __call__(self):
        res = {}
        res['log_bin'] = Env.database.get_variables_value("log_bin")
        if res['log_bin'] == "ON":
            variables = ['binlog_format', 'sync_binlog', 'expire_logs_days', 'datadir']
            res.update(Env.database.get_multi_variables_value(*variables))
            res['binlog_size'] = Env.database.get_binlog_size()

        res['sync_binlog'] = int(res['sync_binlog'])
        res['expire_logs_days'] = int(res['expire_logs_days'])

        res['disk_capacity'] = get_disk_capacity(res.pop('datadir'))

        return res
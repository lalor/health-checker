# -*- coding:UTF-8 -*-
__author__ = 'hzlaimingxing'

import logging


from health_checker.client.env import Env


LOG = logging.getLogger(__name__)


class CheckConnections(object):

    def __init__(self, params):
        self.params= params

    def __call__(self):

        res = Env.database.get_multi_variables_value('max_connections', 'innodb_buffer_pool_size')

        res['max_connections'] = int(res['max_connections'])
        res['innodb_buffer_pool_size'] = int(res['innodb_buffer_pool_size'])

        return res

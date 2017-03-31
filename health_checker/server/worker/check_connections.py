#!/usr/bin/python
#-*- coding: UTF-8 -*-
import logging
from health_checker.server.worker.generic_worker import GenericWorker
from health_checker.server.util import CheckResult
from health_checker.server.worker.advise import Advise
from health_checker.server.util import humanize_bytes


class CheckConnections(GenericWorker):


    @property
    def action(self):
        return self.__class__.__name__

    def execute(self):
        """
        {'action': 'CheckConnections', 'body': {'innodb_buffer_pool_size': 25769803776, 'max_connections': 3000},
         'is_success': True}

        建议每G内存分配最少200个连接，最大350个连接，合理值每G内存300个连接
        """
        result = self.server.client(action=self.action)
        if not result.get('is_success'):
            return
        else:
            self.body = result.get('body')
            self.do_check()

    def do_check(self):
        self.check_max_connections()


    def check_max_connections(self):
        """
            In [1]: 1024 / 200.0
            Out[1]: 5.12

            In [2]: 1024 / 300.0
            Out[2]: 3.4133333333333336

            In [3]: 1024 / 400.0
            Out[3]: 2.56
        """
        innodb_buffer_pool_size = self.body.get('innodb_buffer_pool_size')
        innodb_buffer_pool_size_in_M = innodb_buffer_pool_size / 1024 / 1024.0
        low, up = innodb_buffer_pool_size_in_M / 5.12, innodb_buffer_pool_size_in_M / 2.56
        recommend = innodb_buffer_pool_size_in_M / 3.41

        result = CheckResult.get_result_template(self, CheckResult.high)

        max_connections = self.body.get('max_connections')
        if max_connections < low or max_connections > up:
            result.advise = Advise.max_connection_warning.format(max_connections, humanize_bytes(innodb_buffer_pool_size),
                                                                 int(low), int(up), int(recommend))
            result.score = -result.score

        self.rs.append(result)
#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function
import logging

from health_checker.server.worker.generic_worker import GenericWorker
from health_checker.server.util import CheckResult
from health_checker.server.util import humanize_bytes
from health_checker.server.worker.advise import Advise


LOG = logging.getLogger(__name__)

class CheckRedoLog(GenericWorker):

    @property
    def action(self):
        return self.__class__.__name__

    def execute(self):
        """
        {'action': 'CheckRedoLog', 'body': {'innodb_flush_method': 'O_DIRECT', 'datadir': '/ebs/mysql_data/',
        'disk_capacity': 200039985152L, 'innodb_flush_log_at_trx_commit': 1, 'innodb_log_file_size': 4294967296},
            'is_success': True}
        """

        result = self.server.client(action=self.action)
        if not result.get('is_success'):
            return
        else:
            self.body = result.get('body')
            self.do_check()

    def do_check(self):
        self.check_innodb_flush_log_at_trx_commit()
        self.check_flush_method()
        self.check_redo_log_file_size()

    def check_innodb_flush_log_at_trx_commit(self):
        innodb_flush_log_at_trx_commit = self.body.get('innodb_flush_log_at_trx_commit')

        result = CheckResult.get_result_template(self, CheckResult.high)
        if innodb_flush_log_at_trx_commit != 1 and innodb_flush_log_at_trx_commit != 3:
            result.advise = Advise.innodb_flush_log_at_trx_commit.format(innodb_flush_log_at_trx_commit, 1)
            result.score = -result.score

        self.rs.append(result)

    def check_flush_method(self):
        flush_method = self.body.get("innodb_flush_method")

        result = CheckResult.get_result_template(self, CheckResult.middle)
        if flush_method != "O_DIRECT":
            result.advise = Advise.innodb_flush_method(flush_method, "O_DIRECT")
            result.score = -result.score

        self.rs.append(result)

    def check_redo_log_file_size(self):
        redo_log_file_size = self.body.get('innodb_log_file_size')
        disk_capacity = self.body.get('disk_capacity')

        result = CheckResult.get_result_template(self, CheckResult.high)
        low, up = self._limit_for_redo_log_file_size()
        if redo_log_file_size < low or redo_log_file_size > up:
            result.advise = Advise.innodb_log_file_size.format(humanize_bytes(disk_capacity),
                                                               humanize_bytes(redo_log_file_size),
                                                               humanize_bytes(low),
                                                               humanize_bytes(up))
            result.score = -result.score

        self.rs.append(result)

    def _limit_for_redo_log_file_size(self):
        """
            * 存储空间0~20G，建议redo为128M到256M
            * 存储空间为20~50G，建议redo为256M到512M
            * 存储空间为50~100G，建议redo为512M到1G
            * 存储空间为100G+，建议redo为1G到4G
        """
        g = 1024 * 1024 * 1024
        m = 1024 * 1024

        disk_capacity = self.body.get('disk_capacity')
        if disk_capacity <= 20*g:
            return (128*m, 256*m)
        elif disk_capacity <= 50*g:
            return (256*m, 512*m)
        elif disk_capacity <= 100*g:
            return (512*m, 1*g)
        else:
            return (1*g, 4*g)
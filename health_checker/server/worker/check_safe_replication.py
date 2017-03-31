#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function
from health_checker.server.worker.generic_worker import GenericWorker
from health_checker.server.worker.advise import Advise
from health_checker.server.util import CheckResult


class CheckSafeReplication(GenericWorker):

    @property
    def action(self):
        return self.__class__.__name__

    def execute(self):

        result = self.server.client(action=self.action)
        if not result.get('is_success'):
            return
        else:
            self.body = result.get('body')
            is_slave = self.body.get('is_slave')
            if not is_slave:
                return
            else:
                self.do_check()

    def do_check(self):
        self.check_io_thread()
        self.check_sql_thread()
        self.check_relay_log_info_repository()
        self.check_relay_log_recovery()

    def check_io_thread(self):
        slave_io_running = self.body.get("slave_io_running")
        last_io_error = self.body.get("last_io_error")

        result = CheckResult.get_result_template(self, CheckResult.middle)
        if slave_io_running.lower() != "yes":
            result.advise = Advise.slave_io_running_error
            result.score = -result.score

        self.rs.append(result)


        result = CheckResult.get_result_template(self, CheckResult.middle)
        if last_io_error:
            result.advise = Advise.last_io_error
            result.score = -result.score

        self.rs.append(result)

    def check_sql_thread(self):
        slave_sql_running = self.body.get("slave_sql_running")
        last_sql_error = self.body.get("last_sql_error")

        result = CheckResult.get_result_template(self, CheckResult.middle)
        if slave_sql_running.lower() != "yes":
            result.advise = Advise.slave_sql_running_error
            result.score = -result.score

        self.rs.append(result)

        result = CheckResult.get_result_template(self, CheckResult.middle)
        if last_sql_error:
            result.advise = Advise.last_sql_error
            result.score = -result.score

        self.rs.append(result)

    def check_relay_log_recovery(self):
        relay_log_recovery = self.body.get("relay_log_recovery")

        result = CheckResult.get_result_template(self, CheckResult.middle)
        if relay_log_recovery != "ON":
            result.advise = Advise.relay_log_recovery(relay_log_recovery, "ON")
            result.score = -result.score

        self.rs.append(result)

    def check_relay_log_info_repository(self):

        relay_log_info_repository = self.body.get("relay_log_info_repository")

        result = CheckResult.get_result_template(self, CheckResult.middle)
        if relay_log_info_repository != "TABLE":
            result.advise = Advise.relay_log_info_repository(relay_log_info_repository, "TABLE")
            result.score = -result.score

        self.rs.append(result)
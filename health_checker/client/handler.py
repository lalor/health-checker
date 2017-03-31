#!/usr/bin/python
#-*- coding: UTF-8 -*-
import logging

from health_checker.client.util import lower_case_with_underscores
from health_checker.client.action.check_binary_logs import CheckBinaryLogs
from health_checker.client.action.check_connections import CheckConnections
from health_checker.client.action.check_redo_log import CheckRedoLog
from health_checker.client.action.check_safe_replication import CheckSafeReplication


LOG = logging.getLogger(__name__)


class MsgHandler(object):
    def fetch_action_func(self, action):
        func_name = lower_case_with_underscores(action)
        func = getattr(self, func_name, None)
        return func

    def execute(self, action, params):
        func = self.fetch_action_func(action)
        if func is None:
            return False, "Action not found, {0}".format(action)
        return func(params)


class SyncMsgHandler(MsgHandler):

    def check_binary_logs(self, msg):
        return CheckBinaryLogs(msg)()

    def check_connections(self, msg):
        return CheckConnections(msg)()

    def check_redo_log(self, msg):
        return CheckRedoLog(msg)()

    def check_safe_replication(self, msg):
        return CheckSafeReplication(msg)()
# -*- coding:UTF-8 -*-
import logging

from health_checker.client.database.connection_pool import ConnectionPool
from health_checker.client.util import check_required_args

LOG = logging.getLogger(__name__)


class DatabaseManager(object):

    @check_required_args(['user', 'password', 'host', 'port'])
    def __init__(self, **kwargs):
        self.pool = ConnectionPool(**kwargs)

    def exec_sql(self, sql):
        LOG.debug("execute sql : {0}".format(sql))
        return self.pool.exec_sql(sql)

    def get_binlog_size(self):
        """
        mysql> show master logs;
        +------------------+-----------+
        | Log_name         | File_size |
        +------------------+-----------+
        | mysql-bin.000003 | 622858092 |
        | mysql-bin.000004 |      1408 |
        +------------------+-----------+
        2 rows in set (0.00 sec)
        """
        sql = "show master logs"
        rows = self.exec_sql(sql)
        return sum(long(row[1]) for row in rows)


    @property
    def is_slave(self):
        rows = self.exec_sql('show slave status')
        return bool(rows)

    def get_slave_status_dict(self):
        rows = self.exec_sql('show slave status')
        return dict(rows)

    def get_variables_value(self, variable):
        sql = "show variables like '{0}'".format(variable)
        rows = self.exec_sql(sql)
        return rows[0][1]

    def sessions(self):
        """
         获取数据库的当前连接数
        """
        sql = 'show processlist'
        rows = self.exec_sql(sql)
        return len(rows)

    def get_multi_variables_value(self, *args):
        res = {}
        for item in args:
            res[item] = self.get_variables_value(item)
        return res
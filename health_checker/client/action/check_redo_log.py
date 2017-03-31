__author__ = 'hzlaimingxing'


import logging


from health_checker.client.env import Env
from health_checker.client.util import get_disk_capacity


LOG = logging.getLogger(__name__)


class CheckRedoLog(object):

    def __init__(self, params):
        self.params= params
        self.res = {}


    def __call__(self):
        res = {}
        variables = ['innodb_log_file_size', 'innodb_flush_log_at_trx_commit', 'innodb_flush_method', 'datadir']
        res.update(Env.database.get_multi_variables_value(*variables))

        res['disk_capacity'] = get_disk_capacity(res.pop('datadir'))

        res['innodb_flush_log_at_trx_commit'] = int(res['innodb_flush_log_at_trx_commit'])
        res['innodb_log_file_size'] = int(res['innodb_log_file_size'])

        return res
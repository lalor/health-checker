#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function

import argparse
import logging
import logging.config
import os
import sys
import traceback

pkg_root = os.path.realpath(os.path.join(os.path.realpath(__file__),
                                         os.path.pardir,
                                         os.path.pardir))
sys.path.append(pkg_root)

from health_checker.client.env import Env
from health_checker.client.database.mysql import DatabaseManager
from health_checker.client.client import Client

from health_checker.server.health_checker_server import HealthCheckerServer



log_cnf = os.path.join(pkg_root, 'conf', 'logging.cnf')
logging.config.fileConfig(log_cnf, disable_existing_loggers=False)
LOG = logging.getLogger(__name__)


def _argparse():
    """
    argument parser
    """
    parser = argparse.ArgumentParser(description='health checker for MySQL database')
    parser.add_argument('--host', action='store', dest='host', required=True,
                        help='connect to host')
    parser.add_argument('--user', action='store', dest='user', required=True,
                        help='user for login')
    parser.add_argument('--password', action='store', dest='password',
                        required=True, help='password to use when connecting to server')
    parser.add_argument('--port', action='store', dest='port', default=3306,
                        type=int, help='port number to use for connection or 3306 for default')
    parser.add_argument('--conn_size', action='store', dest='conn_size', default=5,
                        type=int, help='how much connection for database usage')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    return parser.parse_args()


def main():
    """ entry point """
    try:
        parser = _argparse()
        # d = dict(host="59.111.124.115", user='laimingxing', password='laimingxing', port=3306, size=3)
        Env.database = DatabaseManager(host=parser.host, user=parser.user, password=parser.password, port=parser.port)

        server = HealthCheckerServer(Client())
        server.do_health_check()
        server.get_summary()

    except Exception, exc:
        print(exc)
        LOG.error(traceback.format_exc())


if __name__ == '__main__':
    main()

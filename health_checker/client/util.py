# -*- coding: utf8 -*-
import inspect
import logging
import functools
import re

import psutil

LOG = logging.getLogger(__name__)


def lower_case_with_underscores(name):
    """
    convert camel case to under_line case
    CamelCase -> camel_case
    link: (http://stackoverflow.com/questions/1175208/
    elegant-python-function-to-convert-camelcase-to-camel-case)
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def get_disk_capacity(path):
    """
    通过MySQL的变量datadir获取数据盘的路径，再使用psutil获取数据盘的空间
    In [1]: import psutil

    In [2]: psutil.disk_usage('/ebs/mysql_data')
    Out[2]: sdiskusage(total=214643507200, used=16532504576, free=198111002624, percent=7.7)
    """
    return psutil.disk_usage(path).total


def check_required_args(parameters):
    """check parameters of action"""
    def decorated(f):
        """decorator"""
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            """wrapper"""
            func_args = inspect.getcallargs(f, *args, **kwargs)
            kwargs = func_args.get('kwargs')
            for item in parameters:
                if kwargs.get(item) is None:
                    message = "check required args failed, `{0}` is not found in {1}".format(item, f.__name__)
                    LOG.error(message)
                    raise Exception(message)

            return f(*args, **kwargs)
        return wrapper
    return decorated
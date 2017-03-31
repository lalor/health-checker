#!/usr/bin/python
#-*- coding: UTF-8 -*-

import itertools

class HealthCheckItem(object):
    #all_check_items = {
    #        'CheckIndex'       : ['CheckPrimaryKey', 'CheckInvalidIndex', 'CheckRedundancyIndex', 'CheckIndexCardinality'],
    #        'CheckParameter'   : ['CheckMemoryParameter', 'CheckRedoLog', 'CheckBinaryLog', 'CheckConnections'],
    #        'CheckReplication' : ['CheckSafeReplication'],
    #        'CheckUserVisit'   : ['CheckMysqlDeadLock', 'CheckSlowLog'],
    #        'CheckSecurity'    : ['CheckPrivileges']
    #        }
    all_check_items = {
            'CheckParameter'   : ['CheckBinaryLog', 'CheckConnections'],
            }
    all_health_points = list(itertools.chain(*all_check_items.viewvalues()))

    @staticmethod
    def get_health_check_catalog():
        return HealthCheckItem.all_check_items.keys()

    @staticmethod
    def get_health_check_point():
        return HealthCheckItem.all_health_points

    @staticmethod
    def get_health_check_point_in_catalog(catalog):
        return HealthCheckItem.all_check_items[catalog]


def main():
    print HealthCheckItem.get_health_check_catalog()
    print len(HealthCheckItem.get_health_check_point())

    for catalog in HealthCheckItem.get_health_check_catalog():
        for point in HealthCheckItem.get_health_check_point_in_catalog(catalog):
            print "{0}:{1}".format(catalog, point)


if __name__ == '__main__':
    main()

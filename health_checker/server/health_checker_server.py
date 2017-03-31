#!/usr/bin/python
#-*- coding: UTF-8 -*-

from __future__ import print_function
from threading import Thread

from health_checker.server.worker import *


class HealthCheckerServer(object):
    """ main class """
    def __init__(self, client):
        self.client = client

        self.workers = []
        for point in ["CheckBinaryLogs", "CheckRedoLog", "CheckConnections", "CheckSafeReplication"]:
            cls = globals()[point]
            self.workers.append(cls(self, "catag", point))

    def do_health_check(self):
        """ map """
        threads = [ Thread(target=w.map) for w in self.workers]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        first, rest = self.workers[0], self.workers[1:]
        for worker in rest:
            first.reduce(worker)

        self.result = first.rs

    def get_summary(self):
        sum_scores = sum([abs(r.score) for r in self.result])
        mins_scores = sum([abs(r.score) for r in self.result if r.score < 0])

        print("sum scores : {0}".format(sum_scores))
        print("mins scores: {0}".format(mins_scores))

        for r in self.result:
            if r.score < 0:
                print(r.name, r.advise)
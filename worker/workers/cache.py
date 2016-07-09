#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import tracer
import worker.workers
LOG = worker.workers.LOG.getChild('cache')
LOG.setLevel('INFO')

import logging
logging.getLogger("tracer").setLevel("INFO")

class CacheWorker(worker.workers.Worker):

    def __init__(self):
        super(CacheWorker, self).__init__()

    def _run(self, job):
        """Create a cache"""
        self._job = job
        self._cbn = job.cbn

        # run until the first receive
        tracer.Tracer(self._cbn.path, str("")).run()
